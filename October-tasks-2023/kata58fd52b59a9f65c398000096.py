def min_and_max(l, d, x):
	m = []
	for i in range(l, d + 1):
		if sum(map(int, list(str(i)))) == x:
			m.append(i)
	return [min(m), max(m)]