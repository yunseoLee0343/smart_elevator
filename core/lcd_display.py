import smbus2
import time

I2C_ADDR = 0x27
LCD_WIDTH = 16
LCD_CHR = 1
LCD_CMD = 0
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0
E_PULSE = 0.0005
E_DELAY = 0.0005

bus = smbus2.SMBus(1)

def lcd_send_byte(bits, mode):
    bits_high = mode | (bits & 0xF0) | 0x08
    bits_low = mode | ((bits << 4) & 0xF0) | 0x08
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, bits | 0b00000100)
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR, bits & ~0b00000100)
    time.sleep(E_DELAY)

def lcd_init():
    lcd_send_byte(0x33, LCD_CMD)
    lcd_send_byte(0x32, LCD_CMD)
    lcd_send_byte(0x06, LCD_CMD)
    lcd_send_byte(0x0C, LCD_CMD)
    lcd_send_byte(0x28, LCD_CMD)
    lcd_send_byte(0x01, LCD_CMD)
    time.sleep(E_DELAY)

def lcd_write_string(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    lcd_send_byte(line, LCD_CMD)
    for char in message:
        lcd_send_byte(ord(char), LCD_CHR)