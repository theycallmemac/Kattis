
def move(letter, cup):

	if letter == 'A' and cup == 1:
		cup = 2
	elif letter == 'A' and cup == 2:
		cup = 1
	elif letter == 'B' and cup == 2:
		cup = 3
	elif letter == 'B' and cup == 3:
		cup = 2
	elif letter == 'C' and cup == 1:
		cup = 3
	elif letter == 'C' and cup == 3:
		cup = 1

	return cup


def main():
    cup = 1
    moves = str(input().strip())
    for letter in moves:
    	answer = move(letter,cup)
    	cup = answer
    print(cup)
if __name__ == '__main__':
	main()
