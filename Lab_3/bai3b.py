def hello(name, loud=False):
	if loud:
		print('HELLO, %s!' % name.upper())
	else:
		print('HELLO, %s' % name)
hello('bob')
hello('fred', loud=True)