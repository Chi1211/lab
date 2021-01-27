n = int(input("Nhập độ dài của list: "))
list = []
for i in range(n):
	list.append(int(input("Nhập list có vị trí {}: ".format(i))))
min_value = list[0]
for i in list:
	if i < min_value:
		min_value = i
print(min_value)