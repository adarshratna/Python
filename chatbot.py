import openai

openai.api_key = "API Key"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # cheaper/freer model
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
