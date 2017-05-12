
def minuspieces(n, m):
    count = 0
    while n != m:
    	count += 1
    	n = n - 1
    count = str(-count)
    return count

def main():

    pieces = input().strip().split()

    required = [1,1,2,2,2,8]
    needed = [0] * 6
    i = 0
    while i < len(needed):
    	if required[i] > int(pieces[i]):
    		needed[i] = required[i] - int(pieces[i])
    		needed[i] = str(needed[i])
    	elif required[i] < int(pieces[i]):
    		needed[i] = minuspieces(int(pieces[i]), required[i])
    	else:
    		needed[i] = str(needed[i])
    	i = i + 1
    answer = (' '.join(needed))
    print(answer)

if __name__ == '__main__':
	main()
