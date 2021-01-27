class Greeter(object):
	#constructor
	def __init__(self, name):
		self.name = name
	#instance method
	def greet(self, loud=False):
		if loud:
			print('hello, %s!' % self.name.upper())
		else:
			print('hello, %s' %self.name)
g = Greeter('Fred')
g.greet()
g.greet(loud=True)

		