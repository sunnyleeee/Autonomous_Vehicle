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


> &nbsp;코로나가 지속됨에 따라 많은 사람들이 오프라인에서의 소비보다 **온라인에서 소비**를 하는 경우가 더 많아졌다. <br>즉, 온라인 소비가 많아짐에 따라 **운송업 업무가 증가**했다. 위드코로나가 시작됨에 따라 기존의 소비습관으로 돌아가 운송업무 양에 문제가 생길 수 있을 것이라고 생각할 수 있다. 하지만 현재 일상이 회복되고 있음에도 **사람들은 집에서 시켜 집에서 받는 문화에 익숙해졌다.** 그리하여 에이블리, SSG 위드 코로나 이후 동일하거나 그 이상의 실적을 올리기도 하였다. 이렇듯 바뀌어진 소비습관을 기반으로 운송업에서 `자율 군집주행`을 적용시킨다면 다방면으로 이점이 있을 것이라 생각하여 시작하게 되었다.
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
   
    <img src="/docs/README_Image/calibration2.png" width="350" height="350">
    <img src="/docs/README_Image/calibration_value.png" width="350" height="350"></br>
    
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
 <p><img src="/docs/README_Image/line_detecting7.png" width="240" height="200"></p>
 * Control_lane
   detect_lane에서 구한 도로 중앙 x좌표를 이용하여 car1 카메라의 중앙이 그와 
   같아지도록 PD 제어를 한다. PD제어를 통해 계산된 모터 제어 값을 car1에 publish한다.</br>

### ROS와 OpenCR을 활용한 자율주행
 * 차선인식 설명 넣기

 </br>

### 중앙관리 시스템을 적용한 군집주행
* 오픈소스 활용 및 알고리즘 수정  

</br>

### 결과
* 결과 확인   

</br>

### 오픈소스 활용 내역 
* Git을 통한 버그/개선사항 수정
* 데모 모델 생성

### 참고문헌

</br></br> 
  
