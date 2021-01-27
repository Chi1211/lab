list = []
n = int(input("Nhập độ dài của list: "))
for i in range(n):
	list.append(int(input("Nhập list có vị trí {}: ".format(i))))
answer = []
for v in list:
	if v % 5 ==0:
		answer.append(v)
if len(answer) == 0:
	answer = [0]
print(answer)