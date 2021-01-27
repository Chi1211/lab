n = int(input("Nhập độ dài của list: "))
list = []
for i in range(n):
	list.append(int(input("Nhập list có vị trí {}: ".format(i))))
answer = 0
for v in list:
	answer += v
print(answer)