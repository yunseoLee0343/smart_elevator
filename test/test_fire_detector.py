from core.fire_detector import detect_fire, init_fire_sensor
import time

if __name__ == "__main__":
    print("🔥 화재 감지 테스트 시작")
    init_fire_sensor()
    for i in range(5):
        fire, msg = detect_fire()
        print(f"[{i+1}] 감지 결과: {msg}")
        time.sleep(2)