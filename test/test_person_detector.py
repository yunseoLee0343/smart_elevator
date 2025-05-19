from core.person_detector import detect_person

if __name__ == "__main__":
    print("👤 사람 감지 테스트 시작 (카메라 ON)")
    result = detect_person()
    print("감지 결과:", "사람 있음" if result else "사람 없음")