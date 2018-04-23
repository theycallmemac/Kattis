
def get_point(x, y, xs, ys):
	if x not in xs:
		xs.append(x)
	elif x in xs:
		xs.remove(x)
	if y not in ys:
		ys.append(y)
	elif y in ys:
		ys.remove(y)

	return xs,ys


def main():

	xs = []
	ys = []
	for i in range(3):
		x, y = map(int, input().split())
		point = get_point(x, y, xs, ys)
	print(xs[0], ys[0])


if __name__ == '__main__':
	main()
