import json

class Test:
	def __init__(self, name, age):
		self.name = name
		self.age = age

test = Test('Jorge', 40)

print(json.dumps(test.__dict__))