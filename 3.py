def XOR(str1,str2):
	result = "".join([chr(ord(i)^ord(j)) for i,j in zip (str1,str2)])
	return result

str1 = raw_input()
str1 = str1.decode("hex")
for i in range(256):
	str2 = chr(i)*len(str1)
	print chr(i), XOR(str1,str2)

#'X' Cooking MC's like a pound of bacon