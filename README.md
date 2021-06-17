# 자율주행자동차 (메이커스 Vol.05)

## Lesson1
- 조립, 모터 구동

### 학습내용
- 오렌지파이 부팅
- 오렌지파이 리눅스OS 환경 
- 파이썬 기본적인 사용법
- 모터 구동법
- 관련코드는 `/home/orangepi/autonomousCar/lesson1` 참고

### 1.개발환경 준비하기
- 주의! 조립은 반드시 오렌지파이의 USB파워선을 뽑은 상태로 진행해야 합니다. 감전이나 오렌지파이 파손을 예방하기 위함
- 준비물: 오렌지파이, 파워선, 마이크로SD, (키보드, 마우스, 모니터)
    - microSD card를 오렌파이에 삽입
    - 오렌지파이와 모니터, 키보드, 마우스 연결(원격터미널 연결 시에는 생략)
    - 오렌지파이 usb파워선 연결

### 2. 파이썬 기본 내용 배우기
- python 파일 실행
```
$ python3 소스파일명.py
```

### 3. 모터 구동 실습
```
# 모터드라이브관련 라이브러리는 관리자권한(sudo)이 필요
# 패스워드는 orangepi
sudo python3 motor1.py
sudo python3 motor_for1.py
sudo python3 motor_for2.py
```

- while 구문의 실행 및 비정상 종료
```
# 비정상 종료: 실행 중 Ctrl + c  키입력
sudo python3 motor_while.py
```

- `motor_while.py` 수정해서 모터 구동 속도 변경 실습
```
hw.motor_one_speed(0)
hw.motor_one_speed(50)
hw.motor_one_speed(100)
hw.motor_one_speed(200)
```

- `motor_while.py` 수정해서 모터 반대로 돌리기 실습
```
# 모터드라이브와 모터연결선을 바꾸었을 때 모터 방향이 바뀌는 것 실습
hw.motor_one_speed(-90) -> hw.motor_one_speed(90)
# or
hw.motor_one_speed(90) -> hw.motor_one_speed(-90)
```

## Lesson2
- 키보드 입력 및 토글
- 직진, 좌회전, 우회전 제어
- 관련코드는 `/home/orangepi/autonomousCar/lesson2` 참고

### 입력
- 키보드 입력
```
# 키보드 입력
$ sudo python3 key1.py

# q 입력시 종료
$ sudo python3 key2.py

# s 입력시 Start 출력
$ sudo python3 key3.py

# s 한 번 더 입력시 Stop 출력, 토글 기능
$ python3 key4.py

# 키보드로 모터 제어
$ sudo python3 key_motor1.py

# 방향키로 모터 제어
$ sudo python3 key_motor2.py
```

### 직진, 좌회전, 우회전 제어
- 직진
```
$ sudo python3 forward.py
```

- 좌회전
```
$ sudo python3 left.py
```

- 우회전
```
$ sudo python3 right.py
```

- 종합
```
$ sudo python3 run.py
```

## Lesson3
- 카메라 구동
- 데이터 수집
- 관련코드는 `/home/orangepi/autonomousCar/lesson3` 참고

### 카메라
- 카메라 구동
```
$ sudo python3 capture1.py
```

- 이미지 저장
```
$ sudo python3 capture2.py
```

- 저장된 이미지 목록
```
$ sudo python3 capture3.py
```

### 데이터 저장
- csv 파일 
```
# 파일 저장
$ sudo python3 savedata1.py

# 연속 저장
$ sudo python3 savedata2.py
```

## Lesson4
- 자율주행자동차 원리
- 자동차 시범 운전
- 자율주행자동차를 위한 훈련데이터 수집 
- 인공지능 훈련 및 검증
- 관련코드는 `/home/orangepi/autonomousCar/lesson4` 참고

### 자율주행자동차 차선유지 기능 구현 원리
- 훈련데이터 수집
- 훈련
- 시뮬레이션
- 테스트

### 데이터 수집
- 시범 운전
```
# s로 토글, q로 종료, r로 데이터 수집
# 화살표로 직진, 좌회선, 우회전
$ sudo python3 keyboard.py 
```

- 훈련데이터 분석
```
$ sudo python3 data_analysis.py
```

- 전처리
```
$ sudo python3 decalcom.py
$ sudo python3 data_analysis.py
```

- 훈련
```
$ sudo python3 train.py
# 확인
$ tensorboard --logdir=./logs –port=6006
```

- 시뮬레이션
```
$ sudo python3 simulate.py
```

- 테스트
```
$ sudo python3 airun.py
```

