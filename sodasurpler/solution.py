
def total_drank(drank, empty, c):
	while c <= empty:
		drank += empty // c
		empty = (empty % c) + (empty // c) 

	return drank


def main():
	e, f, c = input().split()
	e = int(e)
	f = int(f)
	c = int(c)

	drank = 0
	empty = e + f

	drank = total_drank(drank, empty, c)
	print(drank)

if __name__ == '__main__':
	main()

