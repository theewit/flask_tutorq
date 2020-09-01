class MyNumbers:
	def __iter__(self):
		self.x = 1
		return self

	def __next__(self):
		a = self.x
		self.x += 1
		return a

myclass = MyNumbers()
x = iter(myclass)

print(next(x), next(x))