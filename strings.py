def strupr(word):
	small_list = [chr(x) for x in range(97,123)]
	output = ""
	for each in word:
		if each in small_list:
			output += chr((ord(each) - 32))
		else:
			output += each
	return output

def strlwr(word):
	cap_list = [chr(x) for x in range(65,91)]
	output = ""
	for each in word:
		if each in cap_list:
			output += chr((ord(each) + 32))
		else:
			output += each
	return output

