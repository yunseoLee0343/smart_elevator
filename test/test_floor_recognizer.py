from core.floor_recognizer import recognize_floor

if __name__ == "__main__":
    print("🎤 Floor voice recognition test")
    floor = recognize_floor()
    if floor:
        print("Recognized floor:", floor)
    else:
        print("Recognition failed")
