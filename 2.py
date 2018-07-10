def XOR(str1,str2):
	result = "".join([chr(ord(i)^ord(j)) for i,j in zip (str1,str2)])
	return result

str1 = raw_input("String1").decode("hex")
str2 = raw_input("String2").decode("hex")
print XOR(str1,str2).encode("hex")

#the kid don't play