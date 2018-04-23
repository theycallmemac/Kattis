from sys import stdin

def main():


	submissives = {"A":11,"K":4,"Q":3,"J":2,"T":10}
	dominants = {"A":11,"K":4, "Q":3,"J":20,"T":10,"9":14}

	_, suit = stdin.readline().strip().split()

	total = 0

	for card in stdin:
		card = card.strip()
		if card[1] == suit:
			if card[0] in dominants:
				total += dominants[card[0]]
		else:
			if card[0] in submissives:
				total += submissives[card[0]]

	print(total)


if __name__ == '__main__':
	main()
