<h1 align="center">The Truck Platooning Using Autonomous Driving  </h1>


<h4 align="center">Turtle Bot을 활용한 화물차 자율 군집주행</h4>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 
 
 
<p align= "center">
<img src=/docs/README_Image/readme.png width=600 height=400></p> 
 
<h3 align="center">Team Member</h3>

<div align = "center">
홍형락<a href ="https://github.com/blackbeandu" ><img alt = "홍형락" src = "https://img.shields.io/badge/github-go-yellow?logo=github" ></a>
이선재<a href ="https://github.com/sunnyleeee" ><img alt = "이선재" src = "https://img.shields.io/badge/github-go-blue?logo=github" ></a>
장동현<a href ="https://github.com/J-DongHyeon" ><img alt = "장동현" src = "https://img.shields.io/badge/github-go-green?logo=github" ></a>
</div>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


------------------------------------------

# 1. 기획 계기
<p align= "center">
<img src=/docs/README_Image/SUB.png width=600 height=400></p> 


> &nbsp;코로나가 지속됨에 따라 많은 사람들이 오프라인에서의 소비보다 **온라인에서 소비**를 하는 경우가 더 많아졌다. <br>즉, 온라인 소비가 많아짐에 따라 **운송업 업무가 증가**했다. 위드코로나가 시작됨에 따라 기존의 소비습관으로 돌아가 운송업무 양에 문제가 생길 수 있을 것이라고 생각할 수 있다. 하지만 현재 일상이 회복되고 있음에도 **사람들은 집에서 시켜 집에서 받는 문화에 익숙해졌다.** 그리하여 에이블리, SSG 위드 코로나 이후 동일하거나 그 이상의 실적을 올리기도 하였다. 이렇듯 바뀌어진 소비습관을 기반으로 운송업에서 `중앙 집중형 자율 군집주행`을 적용시킨다면 인건비 및 연비 감소 등 여러 이점이 있을 것이라 생각하였다.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 
# 2. 사용기기 및 개발환경

<p align= "center">
 <img src="/docs/README_Image/turtlebot3-burger.png" width="400" height="400"></p>
 
> &nbsp;`TurtleBot3 Burger`를 사용하였습니다. TurtleBot3은 교육, 연구, 취미 및 제품 프로토타이핑에 사용하기 위한 작고 저렴하며 프로그래밍 가능한 **ROS 기반 모바일 로봇**입니다.
> TurtleBot3는 기계 부품을 어떻게 재구성하고 컴퓨터, 센서 등의 옵션 부품을 사용하느냐에 따라 다양한 방식으로 `커스터마이징`이 가능하여 체택하게 되었습니다.
</br></br>

<p align= "center">
<img src="/docs/README_Image/inv.png" width="700" height="250"></p>  

>  &nbsp;`ROS`로 Turtle Bot의 구동을 진행시켰습니다. ROS를 위하여 Ubuntu 16.04 LTS Desktop 이미지를 사용하였습니다. 
>  (18.04는 호환 오류가 발생)

</br></br>

# 3. 프로젝트 내용  
### OpenCV를 이용한 Line-detection
 * Intrinsic_calibration </br>
   <img src="/docs/README_Image/calibration0.png" width="350" height="225">
   <img src="/docs/README_Image/calibration1.png" width="350" height="225"></p>
   checkerboard를 이용하여 카메라의 내부 파라미터를 구한다. 계산된 카메라 내부 파라미터를 <mark>.yaml</mark> 파일에 저장한다.</br></br>
   
    <img src="/docs/README_Image/calibration2.png" width="300" height="300">
    <img src="/docs/README_Image/calibration_value.png" width="300" height="300"></br>
    
 >  &nbsp; TurtleBot이 내부 파라미터를 구하는 모습
 </br>
 <hr>
   <p>
   <img src="/docs/README_Image/line_detecting3.png" width="200" height="160">
   <img src="/docs/README_Image/line_detecting4.png" width="200" height="160">
   <img src="/docs/README_Image/line_detecting5.png" width="200" height="160">
   <img src="/docs/README_Image/line_detecting6.png" width="200" height="160"><p>
 
 >  &nbsp; 좌측부터 1번

 * Extrinsic_calibration (🖼 1, 2)</br> 
   카메라가 보는 각도의 image에 특정 4개 좌표를 구한다. openCV의 findHomography 함수를 이용하여 앞서 구한 특정 4개의 좌표를 내가 원하는 4개 </br>
   좌표로 변환 시키는 변환 행렬을 구한다. 이 변환 행렬을 기존 이미지에 적용하여 Top View 이미지 형태로 변환 시킨다.
 * Detect_lane (🖼 3, 4)</br>
   도로 Top View 이미지를 BGR모델에서 HSV모델로 변형 시킨 후, 노란색과 하얀색의 HSV 
   범위를 적당하게 설정하여 왼쪽, 오른쪽 차선 마스크를 구한다.
 <p align = "center"><img src="/docs/README_Image/line_detecting7.png" width="340" height="300"></p>
 
 >  &nbsp; **[결과]** 각 마스크를 이용하여 왼쪽 차선, 오른쪽 차선 x좌표를 구하고, 이 두 값의 평균으로 도로 중앙에 해당하는 x좌표를 구한다
 </br>

### ROS와 OpenCR을 활용한 자율주행 </br>
<p align= "center">
<img src="/docs/README_Image/diagram4.png" width="700" height="250"></p>

* Control_lane </br>
   Detect_lane에서 구한 도로 중앙 x좌표를 이용하여 car1 카메라의 중앙이 그와 
   같아지도록 PD 제어를 한다. PD제어를 통해 계산된 모터 제어 값을 car1에 publish한다.</br>

 </br>

### 중앙관리 시스템을 적용한 자율 군집주행

<p align= "center">
<img src="/docs/README_Image/diagram0.png" width="700" height="380"></p>
Car1은 자신의 카메라를 켜고 raw image data을 Remote PC로 보낸다. Remote PC로부터 차선 인식 후 계산된 모터 제어 값을 subscribe 하여 자율 주행을 한다. Car2는 카메라를 off하고 자율 주행 하지 않은 채로 Car1에 의존적으로 자율 군집주행을 한다. 이기종 하드웨어 간의 원활한 데이터 송수신, 처리를 위해 로봇 응용 소프트웨어 개발에 주로 사용되는 메타운영체제인 ROS 를 이용하였다. 위 사진은 Remote PC가 차선 인식과 군집 주행을 위한 연산 등의 메인 처리를 담당하며, Car1,2의 raspberry pi는 카메라 이미지, 라이다 센서 등의 데이터를 Remote PC로 publish 하거나 모터 제어 값을 Remote PC로부터 subscribe 하는 구조를 도식화 한 것이다.

</br>

### 군집주행 알고리즘

</br>

### 결과
* 시연영상
<p align="center"><img src="/docs/README_Image/video_result.gif" width="768" height ="432"></p>  

</br>

# 4. 오픈소스 활용 내역 </br>
1️⃣ https://github.com/ROBOTIS-GIT/turtlebot3_autorace/tree/master/turtlebot3_autorace_camera</br>
2️⃣ https://github.com/ROBOTIS-GIT/turtlebot3_autorace/tree/master/turtlebot3_autorace_detect</br>
3️⃣ https://github.com/ROBOTIS-GIT/turtlebot3_autorace/tree/master/turtlebot3_autorace_control</br>
4️⃣ https://github.com/ROBOTIS-GIT/turtlebot3_applications/tree/master/turtlebot3_follower</br>
5️⃣ https://github.com/ROBOTIS-GIT/turtlebot3_applications/tree/master/turtlebot3_follow_filter</br>


# 5. 참고문헌
 📙 이설영, et al. 자율협력주행 환경에서 군집주행에 따른 효과분석. 대한교통학회 학술대회지, 2017, 423-428.</br>
 📙 조영; 권경주; 오철. 고속도로 화물차 군집주행 적용구간 선정 연구. 대한교통학회지, 2018, 98-111.</br>
 📙 김예진, 정하림, 고우리, 박중규, 윤일수. 메타분석을 이용한 화물차 군집주행의 효과 분석. 한국ITS학회논문지, 2022, 76-90.</br>
</br></br> 
  
