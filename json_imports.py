import json

file = open('res/sample_json.txt')
file_contents = json.load(file)

file.close()

print(file_contents['id'])
