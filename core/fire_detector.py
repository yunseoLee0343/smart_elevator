import board
import adafruit_dht
import RPi.GPIO as GPIO
import time

MQ2_PIN = 17
TEMP_THRESHOLD = 10.0
GAS_DETECTED = GPIO.LOW

# Initialize DHT22 sensor
def init_dht_sensor(pin=board.D4):
    return adafruit_dht.DHT22(pin)

# Initialize MQ2 sensor GPIO
def init_gas_sensor(pin=MQ2_PIN):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

def detect_fire(dht_sensor, gas_pin=MQ2_PIN):
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
        gas_status = GPIO.input(gas_pin)

        if temperature is not None and temperature > TEMP_THRESHOLD and gas_status == GAS_DETECTED:
            msg = f"🔥 Fire detected! Temperature: {temperature:.1f}°C, Gas detected"
            return True, msg
        else:
            gas_msg = 'Detected' if gas_status == GAS_DETECTED else 'Normal'
            msg = f"Normal. Temperature: {temperature:.1f}°C, Gas status: {gas_msg}"
            return False, msg

    except RuntimeError as e:
        # Occasional read errors, ignore and retry recommended
        return False, f"[WARN] Sensor read error: {e}"
    except Exception as e:
        return False, f"[ERROR] Sensor error: {e}"

def cleanup():
    GPIO.cleanup()