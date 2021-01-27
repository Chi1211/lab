def sets1():
	animals = {'cat', 'dog'}
	print('cat' in animals)
	print('fish' in animals)
	animals.add('fish')
	print('fish' in animals)
	print(len(animals))
	animals.add('cat')
	print(len(animals))
	animals.remove('cat')
	print(len(animals))

def sets2():
	animals = ['cat', 'dog', 'monkey']
	for idx, animal in enumerate(animals):
		print('#%d: %s' % (idx + 1, animal))

def sets3():
	from math import sqrt
	nums = {int(sqrt(x)) for x in range(30)}
	print(nums)

print(sets3())