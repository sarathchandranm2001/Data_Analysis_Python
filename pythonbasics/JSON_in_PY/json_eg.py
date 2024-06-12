import json
x='{"name":"Sarath","age":"22"}'
y=json.loads(x)
print(y)
print(type(y))
z=json.dumps(y)
print(type(z))