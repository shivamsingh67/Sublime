if __name__ == '__main__':
	string = str(input())

	ans = list()

	map = {}

	n = len(string)

	for data in range(n):
		if string[data] not in map:
			map[string[data]] = 1
		else:
			map[string[data]] += 1

	for data in map:
		if map[data] > 1:
			ans.append(data)

	for data in ans:
		print(data, end=' ')

	# print(ans)

