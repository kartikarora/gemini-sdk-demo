import time

import google.generativeai as genai
from google.generativeai.types import TunedModelState

base_model = [
    m for m in genai.list_models()
    if "createTunedModel" in m.supported_generation_methods][0]

name = 'generate-num-plus-one-002'
operation = genai.create_tuned_model(
    source_model=base_model.name,
    training_data=[
        {
            'text_input': '1',
            'output': '2',
        }, {
            'text_input': '3',
            'output': '4',
        }, {
            'text_input': '-3',
            'output': '-2',
        }, {
            'text_input': 'twenty two',
            'output': 'twenty three',
        }, {
            'text_input': 'two hundred',
            'output': 'two hundred one',
        }, {
            'text_input': 'ninety nine',
            'output': 'one hundred',
        }, {
            'text_input': '8',
            'output': '9',
        }, {
            'text_input': '-98',
            'output': '-97',
        }, {
            'text_input': '1,000',
            'output': '1,001',
        }, {
            'text_input': '10,100,000',
            'output': '10,100,001',
        }, {
            'text_input': 'thirteen',
            'output': 'fourteen',
        }, {
            'text_input': 'eighty',
            'output': 'eighty one',
        }, {
            'text_input': 'one',
            'output': 'two',
        }, {
            'text_input': 'three',
            'output': 'four',
        }, {
            'text_input': 'seven',
            'output': 'eight',
        }
    ],
    id=name,
    epoch_count=100,
    batch_size=4,
    learning_rate=0.001,
)
model = genai.get_tuned_model(f'tunedModels/{name}')
state = model.state

for status in operation.wait_bar():
    if status is not TunedModelState.ACTIVE:
        time.sleep(1)
    else:
        break

if state is TunedModelState.ACTIVE:
    print(f"Model {name} is ready for use")
