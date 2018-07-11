import string as string
def XOR(str1,str2):
	result = "".join([chr(ord(i)^ord(j)) for i,j in zip (str1,str2)])
	return result

def detect(str1):
	for i in range(256):
		str2 = chr(i)*len(str1)
		pt1 = XOR(str1,str2)
		pt2 = ""
		for c in pt1:
			if c in string.printable:
				pt2 += c
		if pt1 == pt2:
			print chr(i), pt1

str1 = raw_input()
str1 = str1.decode("hex")
detect(str1)

#'X' Cooking MC's like a pound of bacon