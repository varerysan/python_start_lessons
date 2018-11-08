import json

data = {"data": 100, "value": 200}

result = json.dumps(data)

print("result converted to string={}=".format(result))

input_data = '{"values":[10,20,30],"data": {"name1":123,"name2":"hello"}}'

data2 = json.loads(input_data)

print("python data data2:")
