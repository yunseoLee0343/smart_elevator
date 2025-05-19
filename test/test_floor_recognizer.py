from core.floor_recognizer import recognize_floor

if __name__ == "__main__":
    print("🎤 층수 음성 인식 테스트")
    floor = recognize_floor()
    if floor:
        print("인식된 층수:", floor)
    else:
        print("인식 실패")