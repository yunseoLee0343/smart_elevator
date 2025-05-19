from lcd_display import lcd_init, lcd_write_string
import time

if __name__ == "__main__":
    print("📟 LCD 테스트 시작")
    lcd_init()
    lcd_write_string("LCD 테스트 중...", 0x80)
    time.sleep(2)
    lcd_write_string("완료!", 0xC0)