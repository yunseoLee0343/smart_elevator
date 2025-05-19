import speech_recognition as sr
from lcd_display import *

recognizer = sr.Recognizer()
mic = sr.Microphone()

def recognize_floor():
    lcd_init()
    lcd_write_string("Recognizing floor...", 0x80)

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Please speak (e.g., 3rd floor)")
            audio = recognizer.listen(source, timeout=5)

        # Recognize with pocketsphinx (offline speech recognition)
        text = recognizer.recognize_sphinx(audio, language='ko-KR')  # Requires Korean model installation
        print(f"[INFO] Recognized text: {text}")

        recognized_floor = None
        if "지하" in text:
            recognized_floor = "B" + ''.join(filter(str.isdigit, text))
        else:
            digits = ''.join(filter(str.isdigit, text))
            recognized_floor = digits + "F" if digits else None

        if recognized_floor:
            lcd_write_string("Floor: " + recognized_floor, 0x80)
            return recognized_floor
        else:
            lcd_write_string("Recognition failed", 0x80)
            return None

    except sr.UnknownValueError:
        lcd_write_string("Speech recognition failed", 0x80)
    except sr.RequestError as e:
        lcd_write_string("API error", 0x80)
    except Exception as e:
        lcd_write_string("Error occurred", 0x80)
        print(f"[ERROR] Exception occurred: {e}")
    return None