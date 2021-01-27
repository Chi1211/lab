list = []
n=int(input("Nhập độ dài của list: "))
for i in range(n):
	list.append(int(input("Nhập list có vị trí {}: ".format(i))))
for i in range(len(list)):
	for j in range(i):
		if list[i] < list[j]:
			tmp = list[i]
			list[i] = list[j]
			list[j] = tmp
print(list)