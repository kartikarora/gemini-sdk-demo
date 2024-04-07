import google.generativeai as genai
import PIL.Image

from utils import API_KEY

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('models/gemini-pro-vision')

img = PIL.Image.open('assets/instrument.jpg')

# Preview the image
# (thumb := img.copy()).thumbnail((200, 200))
# thumb.show()


response = model.generate_content(
    ['What instrument is this?',
     img,
     'What kinds of music would use it?'])

print(response.text)
# This is a pipe organ. Organs are used in all kinds of music, but they are most commonly associated with classical
# music and church music.
