def main():
    n = int(input())
    i = 0
    X = 0

    while (i < n):
        number = int(input())
        base = number//10
        power = int(str(number)[len(str(number))-1])
        X = X + (base ** power)
        i = i + 1
    print(X)
    
if __name__ == '__main__':
	main()
