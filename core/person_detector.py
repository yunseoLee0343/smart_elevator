import cv2
from picamera2 import Picamera2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detect_person():
    picam2 = Picamera2()
    picam2.configure(picam2.create_still_configuration())
    picam2.start()

    try:
        frame = picam2.capture_array()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        boxes, _ = hog.detectMultiScale(gray, winStride=(8, 8))
        return len(boxes) > 0
    except Exception as e:
        print(f"[ERROR] Person detection failed: {e}")
        return False
    finally:
        picam2.stop()