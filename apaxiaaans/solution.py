def main():

    word = input().strip()
    i = 0

    output = []

    output.append(word[0])

    while i < len(word) - 1:
    	if word[i] != word[i+1]:
    		output.append((word[i+1]))
    	i = i +1

    print(''.join(output))
    
if __name__ == '__main__':
    main()
