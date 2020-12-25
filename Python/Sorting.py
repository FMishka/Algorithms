def Smallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def Sort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = Smallest(arr)
		newArr.append(arr.pop(smallest)) # Добавление самого маленького элемента и удаление его из старого списка
	return newArr

print(Sort([9,8,7,6,5,4,3,2,1,0]))
