
import sys

def get_mixed_fraction(n,d):
	
	if n == 0 and d == 0:
		sys.exit(0)

	return ("{} {} / {}".format(n//d,n%d,d))

def main():

	for line in sys.stdin:

		fraction_parts = line.split(' ')
		numerator,denominator = int(fraction_parts[0]), int(fraction_parts[1])
    
		print(get_mixed_fraction(numerator,denominator))

if __name__ == '__main__':
	main()
