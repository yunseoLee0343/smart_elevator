import pocketsphinx
from pocketsphinx import LiveSpeech, get_model_path
from core.lcd_display import lcd_init, lcd_write_string

def recognize_floor():
    lcd_init()
    lcd_write_string("Recognizing floor...", 0x80)

    model_path = get_model_path()

    speech = LiveSpeech(
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        hmm=model_path + '/en-us',
        lm=model_path + '/en-us.lm.bin',
        dic=model_path + '/cmudict-en-us.dict'
    )

    recognized_floor = None
    try:
        print("Please speak (e.g., 'third floor')")

        for phrase in speech:
            text = str(phrase).lower()
            print(f"[INFO] Recognized text: {text}")

            # 예시: 'basement 1', 'third floor' 등 간단 매핑
            if "basement" in text or "b" in text:
                digits = ''.join(filter(str.isdigit, text))
                recognized_floor = "B" + digits if digits else "B"
                break
            else:
                digits = ''.join(filter(str.isdigit, text))
                recognized_floor = digits + "F" if digits else None
                if recognized_floor:
                    break

        if recognized_floor:
            lcd_write_string("Floor: " + recognized_floor, 0x80)
            return recognized_floor
        else:
            lcd_write_string("Recognition failed", 0x80)
            return None

    except Exception as e:
        lcd_write_string("Error occurred", 0x80)
        print(f"[ERROR] Exception: {e}")
        return None
