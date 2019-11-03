import json
from pprint import pprint

with open('p3111_timetable.json', 'r', encoding='utf-8') as file:
    input_data = file.read()
    data = json.loads(input_data)

pprint(data)
