import string
import sys

def get_missing(phrase):

    alphabet = list(string.ascii_lowercase)
    missing = []

    for letter in alphabet:
        if letter not in phrase.lower():
            missing.append(letter)

    return missing



def main():

    	n = int(sys.stdin.readline())

    	for i in range(n):
            phrase = sys.stdin.readline().strip()
            missing = get_missing(phrase)

            if len(missing) == 0:
                print("pangram")
            else:
                print("missing", "".join(missing))

if __name__ == "__main__":
	main()
