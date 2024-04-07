import google.generativeai as genai

from utils import API_KEY

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('models/gemini-pro')

resp = model.generate_content(
    'Write the first paragraph of a story about a magic backpack'
)

print(resp.text)
# In the quaint town of Willow Creek...
