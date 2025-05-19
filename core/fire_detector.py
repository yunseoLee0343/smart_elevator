import board
import adafruit_dht
import RPi.GPIO as GPIO
import time

MQ2_PIN = 17
TEMP_THRESHOLD = 10.0
GAS_DETECTED = GPIO.LOW

# DHT22 센서 초기화
def init_dht_sensor(pin=board.D4):
    return adafruit_dht.DHT22(pin)

# MQ2 센서 GPIO 초기화
def init_gas_sensor(pin=MQ2_PIN):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

def detect_fire(dht_sensor, gas_pin=MQ2_PIN):
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
        gas_status = GPIO.input(gas_pin)

        if temperature is not None and temperature > TEMP_THRESHOLD and gas_status == GAS_DETECTED:
            msg = f"🔥 화재 감지됨! 온도: {temperature:.1f}°C, 가스 감지됨"
            return True, msg
        else:
            gas_msg = '감지됨' if gas_status == GAS_DETECTED else '정상'
            msg = f"정상. 온도: {temperature:.1f}°C, 가스 상태: {gas_msg}"
            return False, msg

    except RuntimeError as e:
        # 센서 읽기 실패 시 가끔 발생하는 예외, 무시하고 재시도 권장
        return False, f"[WARN] 센서 읽기 오류: {e}"
    except Exception as e:
        return False, f"[ERROR] 센서 오류: {e}"

def cleanup():
    GPIO.cleanup()

# # 사용 예시
# if __name__ == "__main__":
#     init_gas_sensor()
#     dht_sensor = init_dht_sensor()
#     try:
#         while True:
#             fire, message = detect_fire(dht_sensor)
#             print(message)
#             time.sleep(2)
#     except KeyboardInterrupt:
#         print("프로그램 종료")
#     finally:
#         dht_sensor.exit()
#         cleanup()