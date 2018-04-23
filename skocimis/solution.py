def get_moves(kangaroos):
	moves = kangaroos[1] - kangaroos[0]

	if kangaroos[2] - kangaroos[1] > moves:
		moves = kangaroos[2] - kangaroos[1]

	return moves - 1


def main():

	kangaroos = [int(kangaroo) for kangaroo in input().split(' ')]
	print(get_moves(kangaroos))

if __name__ == '__main__':
	main()
