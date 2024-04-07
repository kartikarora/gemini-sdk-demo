import pathlib
import google.generativeai as genai

from utils import API_KEY

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('models/gemini-pro')

document1 = pathlib.Path('assets/document1.txt').read_text()
document2 = pathlib.Path('assets/document2.txt').read_text()

result1 = model.generate_content(f"""
  Explain how deep-sea life survives.

  Please answer based on the following document:
  {document1}""")

print(result1.text)
# The provided document states that deep-sea life doesn't survive. It is mostly dead. Therefore,
# I cannot provide an explanation on how deep-sea life survives based on this document.

result2 = model.generate_content(f"""
  Explain how deep-sea life survives.

  Please answer based on the following document:
  {document2}""")

print(result2.text)
# Deep-sea life survives by using chemosynthesis instead of photosynthesis to produce energy.
# Chemosynthesis is a process that uses energy released from chemical reactions to create sugars.
# In the deep ocean, these chemical reactions occur around hydrothermal vents in the ocean floor.
