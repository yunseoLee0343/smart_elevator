from core.person_detector import detect_person
from core.fire_detector import detect_fire, init_fire_sensor
from core.floor_recognizer import recognize_floor
from core.lcd_display import lcd_write_string, LCD_LINE_1
import RPi.GPIO as GPIO

if __name__ == "__main__":
    init_fire_sensor()
    try:
        while True:
            if detect_person():
                print("[INFO] Person detected.")
                fire, msg = detect_fire()
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