from core.fire_detector import detect_fire, init_gas_sensor, init_dht_sensor, cleanup
import time

if __name__ == "__main__":
    init_gas_sensor()
    dht_sensor = init_dht_sensor()
    try:
        while True:
            fire, message = detect_fire(dht_sensor)
            print(message)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Program Terminated.")
    finally:
        dht_sensor.exit()
        cleanup()