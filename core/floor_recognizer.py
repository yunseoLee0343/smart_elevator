import speech_recognition as sr
from lcd_display import lcd_init, lcd_write_string

recognizer = sr.Recognizer()
mic = sr.Microphone()

def recognize_floor():
    lcd_init()
    lcd_write_string("층수 인식 중...", 0x80)

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("🎤 말하세요 (예: 3층)")
            audio = recognizer.listen(source, timeout=5)

        text = recognizer.recognize_google(audio, language='ko-KR')
        print(f"[INFO] 인식된 텍스트: {text}")

        recognized_floor = None
        if "지하" in text:
            recognized_floor = "B" + ''.join(filter(str.isdigit, text))
        else:
            digits = ''.join(filter(str.isdigit, text))
            recognized_floor = digits + "F" if digits else None

        if recognized_floor:
            lcd_write_string("층수: " + recognized_floor, 0x80)
            return recognized_floor
        else:
            lcd_write_string("인식 실패", 0x80)
            return None

    except sr.UnknownValueError:
        lcd_write_string("음성 인식 실패", 0x80)
    except sr.RequestError as e:
        lcd_write_string("API 오류", 0x80)
    except Exception as e:
        lcd_write_string("에러 발생", 0x80)
        print(f"[ERROR] 예외 발생: {e}")
    return None