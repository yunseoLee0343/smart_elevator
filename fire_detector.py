import Adafruit_DHT
import RPi.GPIO as GPIO

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
MQ2_PIN = 17
TEMP_THRESHOLD = 10.0
GAS_DETECTED = GPIO.LOW

def init_fire_sensor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MQ2_PIN, GPIO.IN)

def detect_fire():
    try:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        gas_status = GPIO.input(MQ2_PIN)

        if temperature and temperature > TEMP_THRESHOLD and gas_status == GAS_DETECTED:
            return True, f"🔥 화재 감지됨! 온도: {temperature:.1f}°C, 가스 감지됨"
        else:
            return False, f"정상. 온도: {temperature:.1f}°C, 가스 상태: {'감지됨' if gas_status == GAS_DETECTED else '정상'}"
    except Exception as e:
        return False, f"[ERROR] 센서 오류: {e}"
