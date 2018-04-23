def main():
    line = str(input().strip()).split()
    x, y, n = int(line[0]), int(line[1]), int(line[2])
    i = 1
    while i <= n:
    	if i % x == 0 and i % y == 0:
    		print('FizzBuzz')
    	elif i % x == 0:
    		print('Fizz')
    	elif i % y == 0:
    		print('Buzz')
    	else:
    		print(i)
    	i = i + 1
if __name__ == '__main__':
	main()
