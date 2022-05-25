#! /usr/bin/env python

import math
from matplotlib.pyplot import sca
import rospy
import numpy as np
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry
from enum import Enum
from tf.transformations import euler_from_quaternion

class testingLDS() :
    def __init__(self) :
        self.sub_scan = rospy.Subscriber("/scan", LaserScan, self.cb_scan, queue_size = 1)
        self.sub_odom = rospy.Subscriber("/odom", Odometry, self.cb_odom, queue_size=1)
        self.sub_car1_imu = rospy.Subscriber("/car1/imu", Imu, self.cb_car1_imu, queue_size=1)
        self.sub_imu = rospy.Subscriber("/imu", Imu, self.cb_imu, queue_size=1)
        self.sub_cmd_vel = rospy.Subscriber("/car1/cmd_vel", Twist, self.cb_cmdVel, queue_size=1)

        self.pub_cmd_vel = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)

        self.is_exist = False
        self.speed_ratio = 1
        self.straight_distance = 0
        self.distance_state = Enum("distance_state", "idle too_close proper_distance too_far")
        self.now_distance = 'idle'

        self.origin_x = 0
        self.origin_y = 0
        self.currnet_x = 0
        self.current_y = 0

        self.car1_imu_buf = []

        self.my_imu_yaw = 0

        self.imu_offset = 0

        self.last_error = 0

        self.step = Enum("step", "idle start_step dependency_step")
        self.now_step = 'idle'

        rospy.on_shutdown(self.fnShutDown)
        

    def cb_scan(self, scan) :
        self.dist_arr = []

        for i in range(40) :
            if ((scan.ranges[i] < 0.28 and scan.ranges[i] > 0.01)) :
                self.dist_arr.append(scan.ranges[i])
            if ((scan.ranges[i+320] < 0.28 and scan.ranges[i+320] > 0.01)) :
                self.dist_arr.append(scan.ranges[i+320])

        if (len(self.dist_arr) > 0) :
            self.is_exist = True
        else :
            self.is_exist = False

        if (self.is_exist == True) :
            if (min(self.dist_arr) < 0.10) :
                self.now_distance = self.distance_state.too_close.name
                print(self.now_distance)
                self.speed_ratio = 1

            else :
                self.now_distance = self.distance_state.proper_distance.name
                print(self.now_distance)
                self.speed_ratio = 1

        else :
            self.now_distance = self.distance_state.too_far.name
            self.speed_ratio = 1
            print(self.now_distance)
            
        if (self.now_step == self.step.idle.name) :
            self.straight_distance = float (scan.ranges[0])
            print("straight distance : {0}".format(self.straight_distance))


    def cb_cmdVel(self, cmdVel) :

        if (self.straight_distance == 0) :
            print("no car in front")
            return

        if (self.now_step == self.step.idle.name) :
            self.now_step = self.step.start_step.name
        else :
            pass
            

        
    def cb_odom(self, odom) :
        if (self.now_step == self.step.idle.name) :
            self.origin_x = odom.pose.pose.position.x
            self.origin_y = odom.pose.pose.position.y

        elif (self.now_step == self.step.start_step.name) :
            self.current_x = odom.pose.pose.position.x
            self.current_y = odom.pose.pose.position.y

            twist = Twist()
            twist.linear.x = 0.065 * self.speed_ratio
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = 0
            self.pub_cmd_vel.publish(twist)
            

            if (math.sqrt(math.pow(self.current_x - self.origin_x, 2) 
                + math.pow(self.current_y - self.origin_y, 2)) > self.straight_distance) :
                print("------------------------------------------------------")
                twist = Twist()
                twist.linear.x = 0
                twist.linear.y = 0
                twist.linear.z = 0
                twist.angular.x = 0
                twist.angular.y = 0
                twist.angular.z = 0
                self.pub_cmd_vel.publish(twist)
                self.now_step = self.step.dependency_step.name

        elif self.now_step == self.step.dependency_step.name :
            pass

    def cb_car1_imu(self, imu) :

        if (self.now_step == self.step.idle.name) :
            list = [imu.orientation.x, imu.orientation.y, 
                                imu.orientation.z, imu.orientation.w]

            _, _, yaw = euler_from_quaternion(list)

            yaw = yaw * 180 / math.pi
            self.imu_offset = yaw - self.my_imu_yaw

        elif (self.now_step == self.step.start_step.name) : 
            self.car1_imu_buf.append(imu)
  
        elif (self.now_step == self.step.dependency_step.name) : 
            
            self.car1_imu_buf.append(imu)

            list_orientation = [self.car1_imu_buf[0].orientation.x, self.car1_imu_buf[0].orientation.y, 
                                self.car1_imu_buf[0].orientation.z, self.car1_imu_buf[0].orientation.w]

            self.car1_imu_buf.pop(0)

            _, _, car1_imu_yaw = euler_from_quaternion(list_orientation)
            

            car1_imu_yaw = car1_imu_yaw * 180 / math.pi

            kp = 0.034
            kd = 0.037

            print("Car1", car1_imu_yaw)
            print("car2", self.my_imu_yaw)

            if ( ( np.sign(car1_imu_yaw) != np.sign(self.my_imu_yaw + self.imu_offset) )
                                and ( abs(car1_imu_yaw - (self.my_imu_yaw + self.imu_offset)) > 300 ) ) :
                error = (car1_imu_yaw + 360) - (self.my_imu_yaw + self.imu_offset)
            else :
                error = car1_imu_yaw - (self.my_imu_yaw + self.imu_offset)
            
            '''
            if ( ( np.sign(car1_imu_yaw) != np.sign(self.my_imu_yaw + self.imu_offset) )
                                and ( self.my_imu_yaw + self.imu_offset > 170 ) ) :
                error = (car1_imu_yaw + 360) - (self.my_imu_yaw + self.imu_offset)
            else :
                error = car1_imu_yaw - (self.my_imu_yaw + self.imu_offset)
            '''

            print(error)
            angular_z = kp * error + kd * (error - self.last_error)

            self.last_error = error
            twist = Twist()
            twist.linear.x = 0.065 * self.speed_ratio
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = max(angular_z, -2.0) if angular_z < 0 else min(angular_z, 2.0) 
            
            self.pub_cmd_vel.publish(twist) 


    def cb_imu(self, imu) :
        list_orientation = [imu.orientation.x, imu.orientation.y, imu.orientation.z, imu.orientation.w]

        _, _, self.my_imu_yaw = euler_from_quaternion(list_orientation)

        self.my_imu_yaw = (self.my_imu_yaw * 180) / math.pi



        

    def fnShutDown(self):
        rospy.loginfo("Shutting down. cmd_vel will be 0")

        twist = Twist()
        twist.linear.x = 0
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = 0
        self.pub_cmd_vel.publish(twist) 
        
             


    def main(self) :
        rospy.spin()

if __name__ == '__main__' :
    rospy.init_node('test_lds_node')
    node = testingLDS()
    node.main()