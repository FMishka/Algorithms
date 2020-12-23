# Для отсортированного списка
def binary_search(list, item):
	low = 0 # Нижний предел
	high = len(list) - 1 # Врехний предел

	while low <= high:
		mid = (low + high) // 2 # Получаем середину
		guess = list[mid] # Число из середины
		if guess == item: # Если середина равна искомому числу, то оно найдено
			return mid
		elif guess > item: # Если искомое число больше нужного, то верхний предел нужно уменьшить
			high = mid - 1
		else: # Иначе увеличить
			low = mid + 1
	return None

arr = [1, 2, 3, 4, 5, 6]
print(binary_search(arr, 6))
print(binary_search(arr, -1))
