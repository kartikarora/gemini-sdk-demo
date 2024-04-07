import google.generativeai as genai

from utils import API_KEY

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('models/gemini-pro')

chat = model.start_chat()

response = chat.send_message(
    "Hello, what should I have for dinner?"
)

print(response.text)
# ** Main Course **

response = chat.send_message(
    "How do I cook the first one?"
)
