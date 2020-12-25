def Search(OurList: dict, searchable: str):
	low = 0
	high = len(OurList)
	while low < high:
		mid = (low + high) // 2
		Surname = Key(OurList, mid)
		if Surname.upper() == searchable.upper():
			return OurList[Surname]
		elif Surname.upper() < searchable.upper():
			low += 1
		else:
			high -= 1
	return None

def Key(OurList:dict, number: int):
	keys = list(OurList.keys())
	return keys[number]


Surnames = {'a':101,
			'b':102,
			'c':103,
			'd':104,
			'e':105
}

print('a =',Search(Surnames, 'a'))
print('b =',Search(Surnames, 'b'))
print('c =',Search(Surnames, 'c'))
print('d =',Search(Surnames, 'd'))
print('e =',Search(Surnames, 'e'))

