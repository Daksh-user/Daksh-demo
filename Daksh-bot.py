
from openai import OpenAI

# ✅ Replace this with your real OpenAI API key
client = OpenAI(api_key="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

def chat_with_dakshbot():
    print("🤖 DakshBot is online! Type 'exit' to stop chatting.\n")

    messages = [
        {"role": "system", "content": "You are a helpful and intelligent assistant named DakshBot. Answer all questions clearly and respectfully."}
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("DakshBot: bye")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # or use "gpt-4" if your key allows it
                messages=messages
            )
            bot_reply = response.choices[0].message.content
            messages.append({"role": "assistant", "content": bot_reply})
            print(f"DakshBot: {bot_reply}")

        except Exception as e:
            print("DakshBot: Sorry, I ran into an error:\n", e)

if __name__ == "__main__":
    chat_with_dakshbot()