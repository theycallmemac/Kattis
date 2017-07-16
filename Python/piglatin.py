import sys
def main():
	cases = ['a','e','i','o','u','y']
	try:
		for i in range(4000):
			line = str(input()).split(" ")
			if line == [""]:
				break
			piglatin = ""
			for word in line:
				if word[0] in cases:
					word = word + 'yay'
				else:
					i = 0
					while i < len(word):
						if word[i] in cases:
							word = word[i:len(word)] + word[:i] + 'ay'
							break
						i += 1
				piglatin += word + " "
			print(piglatin)
	except EOFError:
		sys.exit()

if __name__ == '__main__':
	main()
