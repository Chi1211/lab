# Cau2
n=int(input("Nhập số cần tinh: "))
def giaithua(n):
	if n==0:
		return 1
	else: 
		return n*giaithua(n-1)
print("Giai thua: {}".format(giaithua(n)))