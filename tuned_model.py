import time

import google.generativeai as genai

name = 'generate-num-plus-one-002'

model = genai.GenerativeModel(model_name=f'tunedModels/{name}')

result = model.generate_content('55')
print(result.text)  # 56

result = model.generate_content('quatre')
print(result.text)  # French 5 is "cinq"

result = model.generate_content('III')
print(result.text)  # Roman numeral 4 is IV

result = model.generate_content('七')
print(result.text)  # Japanese 8 is 八!
