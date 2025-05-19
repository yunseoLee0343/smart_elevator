from core.fire_detector import *
import time

if __name__ == "__main__":
    dht_sensor = init_dht_sensor()
    mq2_channel = init_adc()

    try:
        while True:
            fire, msg = detect_fire(dht_sensor, mq2_channel)
            print(msg)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        cleanup()
