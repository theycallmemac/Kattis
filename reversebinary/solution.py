
def convert_to_binary(n):
	n = str(bin(n))
	return n[2:]


def reverse(b):
	rb = b[::-1]
	return rb


def convert_to_decimal(rb):
	d = int(rb, 2)
	return d

def main():

	n = int(input())
	b = convert_to_binary(n)
	rb = reverse(b)

	d = convert_to_decimal(rb)
	print(d)


if __name__ == '__main__':
	main()
