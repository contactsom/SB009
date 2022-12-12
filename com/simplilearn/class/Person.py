class Person:
	def __init__(self, name , id, age):
		self.name = name
		self.id = id
		self.age = age

	def say_hi(self):
		print('Hello, my name is', self.name)
		print('Hello, my ID is', self.id)
		print('Hello, my Age is', self.age)


p = Person('Nikhil',10,28)
p.say_hi()
