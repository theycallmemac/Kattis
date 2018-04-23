def main():

    line = int(input().strip())
    temps = str(input().strip()).split()
    count = 0
    for i in temps:
    	if int(i) < 0:
    		count += 1
    	else:
    		pass
    print(count)

if __name__ == '__main__':
	main()
