from google import genai

# 1. 내 API 키 설정
client = genai.Client(api_key="AQ.Ab8RN6KXpnT802wwNdz5jtLXd7Mt9n02gnMtfIA8lIGsIZbxXw")

print("====================================")
print("🤖 JaredKim님의 Gemini 챗봇이 시작되었습니다!")
print("종료하고 싶다면 '종료'라고 입력하세요.")
print("====================================")

# 2. 무한 반복(while) 루프 시작
while True:
    # 사용자에게 터미널에서 직접 키보드로 질문을 입력받습니다.
    user_input = input("\n나 ✍️ : ")
    
    # 만약 사용자가 '종료'라고 치면 프로그램을 끝냅니다.
    if user_input == "종료":
        print("🤖 챗봇을 종료합니다. 다음에 또 만나요!")
        break
        
    # 아무것도 입력하지 않고 엔터만 치면 다시 입력을 기다립니다.
    if not user_input.strip():
        continue

    # 사용자가 입력한 따끈따끈한 질문을 Gemini에게 보냅니다.
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_input
    )
    
    # Gemini의 답변을 출력합니다.
    print(f"Gemini 🤖 : {response.text}")