import openai

openai.api_key = "sk-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL"
openai.api_base = "https://4aiu6ctrknfxkoaigkigzh5lwm0cciuc.lambda-url.ap-east-1.on.aws"

def chat_with_bot():
    # สร้างข้อความเริ่มต้นให้โมเดล
    messages = [
        {"role": "system", "content": "You are now chatting with a bot. Type 'exit' to end the conversation."},
    ]

    while True:
        user_input = input("User: ")

        # เมื่อผู้ใช้ป้อน 'exit' ให้สิ้นสุดการสนทนา
        if user_input.lower() == "exit":
            print("Chat ended.")
            break

        # เพิ่มข้อความจากผู้ใช้ใน messages
        messages.append({"role": "user", "content": user_input})

        # ส่ง messages ไปยัง GPT-4 เพื่อรับคำตอบ
        chat_completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )

        # แสดงคำตอบจากโมเดล
        assistant_reply = chat_completion.choices[0].message.content
        print("Bot:", assistant_reply)

        # เพิ่มข้อความจากโมเดลใน messages
        messages.append({"role": "assistant", "content": assistant_reply})

# เริ่มการสนทนากับบอท
chat_with_bot()
