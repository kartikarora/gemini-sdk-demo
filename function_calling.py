import google.generativeai as genai

from assets import API_KEY

genai.configure(api_key=API_KEY)


def multiply(a: float, b: float):
    """Returns a * b."""
    return a * b


model = genai.GenerativeModel(
    model_name='gemini-1.0-pro',
    tools=[multiply])

chat = model.start_chat(
    enable_automatic_function_calling=True)

response = chat.send_message(
    'I have 57 cats, each owns 44 mittens, '
    'how many mittens is that in total?')

# print(response.text)
# The number of mittens in total is 2508.

for content in chat.history:
    part = content.parts[0]
    print(content.role, "->", type(part).to_dict(part))
