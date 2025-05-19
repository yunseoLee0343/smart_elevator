# Raspberry Pi 기반 스마트 엘리베이터 시스템

이 프로젝트는 라즈베리파이로 구현된 **스마트 엘리베이터 시스템**입니다. 다음 기능을 제공합니다:

- **화재 감지** (온도 + 가스)
- **사람 감지** (카메라 기반)
- **음성으로 층수 인식**
- **I2C LCD 디스플레이 표시**

---

## 📦 구성 요소

| 센서 / 장치     | 설명                           |
|----------------|--------------------------------|
| DHT22          | 온도 및 습도 측정               |
| MQ-2           | 가연성 가스 감지                |
| PiCamera2      | 사람 감지 (HOG + OpenCV)       |
| USB 마이크     | 층수 음성 인식 (SpeechRecognition) |
| I2C LCD (16x2) | 현재 상태 표시                  |

---

## 🛠️ 설치 방법

### 1. 라즈비안 설정

```bash
sudo raspi-config
````

* `Interface Options > I2C > Enable`
* `Interface Options > Camera > Enable`

이후 재부팅:

```bash
sudo reboot
```

### 2. 시스템 패키지 설치

```bash
sudo apt update
sudo apt install -y python3-opencv python3-pip i2c-tools libatlas-base-dev
```

### 3. 파이썬 의존성 설치

```bash
pip3 install -r requirements.txt
```

---

## 📂 프로젝트 구조

```
smart_elevator/
├── main.py                  # 메인 실행 파일
├── fire_detector.py         # 온도 + 가스 감지
├── person_detector.py       # 카메라 기반 사람 감지
├── floor_recognizer.py      # 음성 기반 층수 인식
├── lcd_display.py           # I2C LCD 제어
├── requirements.txt
├── tests/                   # 개별 기능 테스트 코드
│   └── ...
```

---

## ▶️ 실행 방법

```bash
cd smart_elevator
python3 main.py
```

**실행 순서:**

1. 사람이 감지되면
2. 화재 유무를 감지하고
3. 화재 없을 시 음성으로 층수 인식
4. 결과를 LCD에 표시

---

## 🧪 테스트

각 기능별 테스트 스크립트는 `tests/` 디렉토리에 있습니다:

```bash
python3 tests/test_fire_detector.py
python3 tests/test_person_detector.py
python3 tests/test_floor_recognizer.py
python3 tests/test_lcd_display.py
```

---

## ⚠️ 주의사항

* 음성 인식은 **인터넷 연결**이 필요합니다 (Google STT 사용).
* `picamera2`는 **라즈비안 Bookworm 이상**에서만 작동합니다.
* 가스 및 온도 임계값은 `fire_detector.py`에서 조정할 수 있습니다.