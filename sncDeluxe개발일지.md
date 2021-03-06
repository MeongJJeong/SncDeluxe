# sncDeluxe

### 개발 목적
 - 설문지 결과를 통계내는데에 수기로 하는 어려움을 해소하고자 개발 시작

### 개발 목표 
 - 설문지 통계를 보다 간편하게 낼 수 있고 엑셀로 결과값을 받을 수 있다.
 - python 언어를 활용한 엑셀 및 데이터 처리에 숙련도 상승 효과를 기대한다.
 - 윈도우 운영체제에서 동작하는것을 목표로 한다.
 - 확장자는 exe, ui는 CLI기반

---

### 개발일지

#### __201109 -ver 0.1__
 - 문제의 갯수와 보기 갯수 그리고 참여 인원의 수를 입력받는다.
 - 최대 보기 수를 5가지로 한정, 딕셔너리 형식으로 받는다.
 - 인원수에 제한을 두고 입력이 종료되면 결과를 출력하는 방식으로 진행.
 문제점
 - 다른 입력값에 대한 excetion 부제
 - 가독성이 너무 불편함
 - 보기 갯수가 5가지 고정형인 부분이 걸림
 -feedback
 - 읽기가 너무 불편하다
 - 보기가 10개 있는 설문지가 존재한다
 - 인원수를 특정하기가 너무 어렵다
 - 엑셀로 저장 기능이 있었으면 좋겠다
 - 무효표를 따로 확인하고싶다

 ---

#### __201110 -ver 0.5__
 - example 딕셔너리를 유동적으로 변수지정 가능하게 변경
 - 입력창에 0 입력시 무효표 추가
 - 입력창에 m 입력시 입력 도중에도 결과값 확인 가능
 - 결과 화면에서 참여인원의 수 와 무효표 수 를 확인가능
 - 결과 화면 가독성 개선 
 - 보기 입력을 0 ~ 10 까지 입력 가능
 - 10의 경우 가독성과 데이터 입출력 의 효율을 위해 t 로 대체

문제점
 - 초반 입력 부분이 너무 복잡하다.
 - 기능키들의 증가에 따라 복잡성이 증가했다.
 - 총 인원 설정에 따른 불편함이 계속된다.
 - 딕셔너리 자료형의 주소값 참조로 인해 전체값에 영향을 준다

feedback
 - 중간 저장기능이 있었으면 좋겠다.
 - 다른키를 입력받았을때 간혹 시스템이 종료된다.
 - 가독성이 떨어진다. 
 - 설명이 잘 이해가 안간다. 
 
---

#### __201111 -ver 0.9.2__
 - 엑셀 출력 기능 추가
 - 기능 키 다수 할당
 - m => 중간점검, s => 엑셀 저장, x => 무효표 
 - help => 도움말, exit => 종료
 - 엑셀 출력 시 이름 지정 가능
 - 덮어쓰기 저장 가능
 - calRate 함수에서 소숫점 지정 가능 
 - snap함수의 설명 변경 
 - help함수의 cli 그래픽 요소 추가

문제점
 - 기능적 구현은 문제 없으나 함수표현이 미흡
 - 파이썬에서의 main함수 이용법이 잘못됐다 생각함
 - 변수명이 상황에 알맞지 않음
 - GUI로 변경을 원함 

feedback
 - 이전에 입력했던 항목에 대한 수정 기능 원함
 - 지금까지의 입력값을 초기화하고 재시작 하는 기능 
 - 가독성이 조금 부족함 
 - GUI.....

feedback plus
 - 엑셀로 저장 시 확률부분을 함수로 만들면 좋을 것 같다.
 - 엑셀 저장 시 제목에 특수문자를 저장하면 저장이 되지 않는다.

---

#### __201228 -ver 0.9.3__
 - 엑셀 출력 시 퍼센트 부분 엑셀함수로 표현
 - 기타 문법 정리


#### __201230 -ver 0.9.4__
 - 엑셀 이름 특수문자 입력 제한 
 - 특수문자 입력 시 제거하고 출력
 - 엑셀 출력 후 소숫점 변경 가능한 셀 참조 추가
 - 엑셀함수용 메서드 추가
 - 추후에 엑셀 기능을 모아 class 생성 필요


</br>
운영체제 -윈도우 </br>
ui -CLI (추후 GUI 지원 예정)