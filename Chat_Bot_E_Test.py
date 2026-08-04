from google import genai
from google.genai import types # AI 설정 기능을 위해 새로운 도구를 하나 더 가져옵니다.

# 1. 내 API 키 설정
client = genai.Client(api_key="AQ.Ab8RN6KXpnT802wwNdz5jtLXd7Mt9n02gnMtfIA8lIGsIZbxXw")

print("====================================")
print("🇺🇸 JaredKim님의 1:1 영어 회화 튜터가 시작되었습니다!")
print("종료하고 싶다면 '종료'라고 입력하세요.")
print("====================================")

# 🚀 [핵심] Gemini에게 비밀 역할을 부여하는 시스템 명령(프롬프트) 설정
english_tutor_config = types.GenerateContentConfig(
    system_instruction="""
    너는 지금부터 JaredKim의 친절한 1:1 원어민 영어 선생님이야.
    규칙은 다음과 같아:
    1. 사용자가 한국어로 문장을 입력하면, 자연스러운 원어민 표현으로 영어 번역을 해줘.
    2. 번역뿐만 아니라, 이 표현이 왜 자연스러운지 아주 쉽고 친절하게 한 줄 설명을 덧붙여줘.
    3. 마지막에는 "한번 따라 해보세요!"라는 격려의 문구를 넣어줘.
    """
)

# 2. 무한 반복 루프 시작
while True:
    user_input = input("\n나 ✍️ : ")
    
    if user_input == "종료":
        print("🤖 See you later! 공부하느라 고생하셨어요.")
        break
        
    if not user_input.strip():
        continue

    # 💡 [핵심 변형] 질문을 보낼 때 위에서 만든 'english_tutor_config'를 함께 구글 서버로 보냅니다!
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_input,
        config=english_tutor_config # AI에게 내 가이드라인(세뇌)을 장착시키는 순간!
    )
    
    print(f"\nGemini 👩‍🏫 : {response.text}")