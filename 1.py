str1 = raw_input("Hex_String")
print str1.decode("hex")
str2 = (str1.decode("hex")).encode("base64")
print str2

#I'm killing your brain like a poisonous mushroom