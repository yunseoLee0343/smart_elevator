from core.person_detector import *
from core.fire_detector import *
from core.floor_recognizer import *
from core.lcd_display import *
import RPi.GPIO as GPIO

if __name__ == "__main__":
    dht_sensor = init_dht_sensor()
    mq2_channel = init_adc()

    try:
        while True:
            if detect_person():
                print("[INFO] Person detected.")
                fire, msg = detect_fire(dht_sensor, mq2_channel)
                print(msg)
                if fire:
                    lcd_write_string("Fire detected!", LCD_LINE_1)
                    break
                else:
                    recognize_floor()
    except KeyboardInterrupt:
        print("Program terminated.")
    finally:
        GPIO.cleanup()