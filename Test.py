from google import genai

# 아래 쌍따옴표 사이에 실제 발급받은 API 키 문자열만 깔끔하게 넣어줍니다.
client = genai.Client(api_key="AQ.Ab8RN6KXpnT802wwNdz5jtLXd7Mt9n02gnMtfIA8lIGsIZbxXw")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='맥북 M1에서 첫 API 호출에 성공했어! 축하해줘.'
)

print(response.text)