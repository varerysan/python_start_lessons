import json

print("Hello")

data = {"data": 100, "value": 200}

result = json.dumps(data)

print("result={}=".format(result))