from core.person_detector import *

if __name__ == "__main__":
    print("Starting person detection test (Camera ON)")
    result = detect_person()
    print("Detection result:", "Person detected" if result else "No person detected")