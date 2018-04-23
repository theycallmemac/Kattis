def main():

    name = input().strip().split('-')
    name = ''.join(name)
    initals = ''

    for letter in name:
    	if letter.isupper():
    		initals += letter

    print(initals)
    
if __name__ == '__main__':
	main()