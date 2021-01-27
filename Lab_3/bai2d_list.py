def list1():
	xs = [3, 1, 2]
	print(xs, xs[2])
	print(xs[-1])
	xs[2] = 'foo'
	print(xs)
	xs.append( 'bar' )
	print(xs)
	x = xs.pop()
	print(x, xs)

def slicing():
	nums = list(range(5))
	print(nums)
	print(nums[2:4])
	print(nums[2:])
	print(nums[:2])
	print(nums[:])
	print(nums[:-1])
	nums[2:4] = [8, 9]
	print(nums)

def loop1():
	animals = ['cat', 'dog', 'monkey']
	for animal in animals:
		print(animal)

def loop2():
	animals = ['cat', 'dog', 'monkey']
	for idx, animal in enumerate(animals):
		print('#%d: %s' % (idx + 1, animal))

def loop3():
	nums = [0, 1, 2, 3, 4]
	squares = []
	for x in nums:
		squares.append(x ** 2)
	print(squares)

def loop4():
	nums = [0, 1, 2, 3, 4]
	squares = [x ** 2 for x in nums]
	print(squares)

def loop5():
	nums = [0, 1, 2, 3, 4]
	even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
	print(even_num_to_square)
print(loop5())
