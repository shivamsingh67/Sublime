def last_occurance(string, target):
	n = len(string)
	st = 0
	en = n - 1
   
	while st <= en:
		mid = st + (en - st) // 2

		if string[mid] == target:
			ans = mid
			st = mid + 1
		elif string[mid] > target:
			en = mid - 1
		else:
			st = mid + 1
	return ans;



def first_occurance(string, target):
	n = len(string)
	st = 0
	en = n - 1
    
	while st <= en:
		mid = st + (en - st) // 2

		if string[mid] == target:
			ans = mid
			en = mid - 1
		elif string[mid] > target:
			en = mid - 1
		else:
			st = mid + 1
	return ans;


def search_element(string, target):
	first = first_occurance(string, target)
	last = last_occurance(string, target)

	ans = list()

	ans.append(first)
	ans.append(last)

	return ans

if __name__ == '__main__':
	string = str(input())
	target = (input())

	ans = list()

	ans = search_element(string, target)

	for data in ans:
		print(data, end=' ')
