def main():
    n = int(input())
    i = 0
    X = 0

    while (i < n):
        number = int(input())
        remainder = number % 2
        if remainder == 0:
        	print(number, "is even")
        else:
        	print(number, "is odd")
        i = i + 1
if __name__ == '__main__':
	main()
