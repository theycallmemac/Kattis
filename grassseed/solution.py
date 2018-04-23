
def main():

	cost = float(input())
	num_lawns = float(input())
	area =0
	total_area = 0

	i = 0
	while i < num_lawns:
		w,l = input().split()
		w, l = float(w), float(l)
		area = w * l
		total_area += area
		i = i + 1

	total_cost = float(total_area * cost)
	print(total_cost)


if __name__ == '__main__':
	main()
