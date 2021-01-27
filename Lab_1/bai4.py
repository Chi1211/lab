def convert_number(n,b):
	if(n<0 or b<2 or b>16):
		return ""
	sb=""
	m=0
	remainder=n

	while (remainder>0):
		if (b>10):
			m=remainder%b
			if(m>=10):
				sb=sb+str(chr(55+m))
			else:
				sb = sb + str(m);
		else:
			sb = sb + str(remainder % b)
		remainder = int(remainder / b)
		return ("".join(reversed(sb))) # dao ngug¢ chudi sb
n = int(input("Nhap so ngyen duong n = "));
print("He so 2 cua so nguyen ", n, "la:", convert_number(n, 2))
print("He so 16 cua so nguyen ", n, "la:", convert_number(n, 16))