import itertools

def permute(string):
	permutations = [ "".join(i) for i in itertools.permutations(string)]
	return permutations


def remove(permutations,n):
	result = sorted(i for i in permutations if int(i) > int(n))
	return result

def minimum(permutations):
	if len(permutations) == 0:
		return 0
	return min(permutations)

def main():

	n = input()
	permutations = permute(n)
	permutations = remove(permutations,int(n))
	print(minimum(permutations))
	
if __name__ == '__main__':
	main()
