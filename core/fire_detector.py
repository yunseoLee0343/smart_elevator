import board
import adafruit_dht
import RPi.GPIO as GPIO
import busio
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

TEMP_THRESHOLD = 10.0

# Initialize DHT22 sensor
def init_dht_sensor(pin=board.D4):
    return adafruit_dht.DHT22(pin)

# Initialize MCP3008 ADC to read analog MQ2 sensor value on channel 0 (A0)
def init_adc():
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
    cs = digitalio.DigitalInOut(board.D5)  # Chip select pin (can be changed)
    mcp = MCP.MCP3008(spi, cs)
    chan = AnalogIn(mcp, MCP.P0)  # Channel 0 = A0
    return chan

def detect_fire(dht_sensor, mq2_channel):
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
        gas_level = mq2_channel.value  # 16-bit ADC value (0~65535)
        gas_voltage = mq2_channel.voltage  # Voltage corresponding to gas level

        # 임계값은 경험적으로 정해야 합니다. 예: 30000 (ADC raw value)
        GAS_THRESHOLD = 30000

        if temperature is not None and temperature > TEMP_THRESHOLD and gas_level > GAS_THRESHOLD:
            msg = f"🔥 Fire detected! Temp: {temperature:.1f}°C, Gas level: {gas_level} (Voltage: {gas_voltage:.2f}V)"
            return True, msg
        else:
            msg = f"Normal. Temp: {temperature:.1f}°C, Gas level: {gas_level} (Voltage: {gas_voltage:.2f}V)"
            return False, msg

    except RuntimeError as e:
        return False, f"[WARN] Sensor read error: {e}"
    except Exception as e:
        return False, f"[ERROR] Sensor error: {e}"

def cleanup():
    GPIO.cleanup()