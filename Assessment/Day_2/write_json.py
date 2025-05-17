import json

data = {"Name":"Siva", "Age":23,"Subjects": ["Maths", "English"]}

with open('data_json.json','w') as file:
    json.dump(data, file, indent=4)