def find_odd_one_out(guests):

	result = 0

	for i in guests:
		i = int(i)
		result ^= i

	return result

def main():

	tests = int(input())
	count = 1

	for i in range(tests):
		num_guests = int(input())
		guests = input().split()
		odd = find_odd_one_out(guests)
		print("Case #" + str(count) + ": " + str(odd))
		count += 1


if __name__ == '__main__':
	main()
