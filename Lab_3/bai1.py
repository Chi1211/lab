def number1():
	x = 3
	print(type(x))
	print(x)
	print(x + 1)
	print(x - 1)
	print(x * 2)
	print(x ** 2)
	x += 1
	print(x)
	x *= 2
	print(x)
	y = 2.5
	print(type(y))
	print(y, y + 1, y ** 2)

def Boolean1():
	t = True
	f = False
	print(type(t))
	print(t and f)
	print(t or f)
	print(not t)
	print(t != f)

def string1():
	hello = 'hello'
	word = "word"
	print(hello)
	print(len(hello))
	hw = hello + '' + word
	print(hw)
	hw12 = '%s %s %d' % (hello, word, 12)
	print(hw12)

def string2():
	s = "hello"
	print(s.capitalize()) 
	print(s.upper()) 
	print(s.rjust(7)) 
	print(s.replace('1', '(e1l)'))
	print(' world '.strip())

print(string2())