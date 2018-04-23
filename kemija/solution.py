
def main():
	sentence = input()
	i = 0
	while i < len(sentence):
		if sentence[i] == 'a' or sentence[i] == 'e' or sentence[i] == 'i' or sentence[i] == 'o' or sentence[i] == 'u':
			sentence = sentence[:i] + sentence[i + 2:]
		i = i + 1
	print(sentence)

if __name__ == '__main__':
	main()
