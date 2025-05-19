from core.lcd_display import *
import time

if __name__ == "__main__":
    print("Starting LCD test")
    lcd_init()
    lcd_write_string("Testing LCD...", 0x80)
    time.sleep(2)
    lcd_write_string("Done!", 0xC0)