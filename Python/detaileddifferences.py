

def main():

	n = int(input())
	inputs = []
	i = 0
	j = 0

	while i < n:
		answer = ""
		word1 = input()
		word2 = input()

		k = 0
		while k < len(word1):
			if word1[k] == word2[k]:
				answer += '.'
			else:
				answer += '*'
			k += 1
		print(word1 + "\n" + word2 + "\n")
		print(answer + "\n")
		i += 1




if __name__ == '__main__':
	main()
