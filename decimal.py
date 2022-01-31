def convert_dec(num):
	nums = str(num)
	if nums.startswith('0b'):
		nums = nums.replace('0b','')
	else:
		pass

	lst = []
	reverse = nums[::-1]

	for n in range(len(reverse)):
		store = (2 ** n) * (int(reverse[n]))
		lst.append(store)

	return sum(lst) 

