def main():

    line = str(input().strip()).split()
    d1, d2 = int(line[0]), int(line[1])

    chances = [0] * (d1+d2 + 1)

    i = 1
    while i <= d1:
    	j = 1
    	while j <= d2:
    		total = i + j
    		chances[total] += 1
    		j = j + 1
    	i = i + 1

    k = 1
    while k < len(chances):
    	if max(chances) == chances[k]:
    		print(k)
    	k = k + 1

if __name__ == '__main__':
	main()
