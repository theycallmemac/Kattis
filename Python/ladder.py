from math import sin, radians, ceil


def get_length(h, v):
    v = radians(v)
    h = h/sin(v)
    return int(ceil(h))



def main():
    n = input().split(' ')
    h = float(n[0])
    v = float(n[1])
    print(get_length(h,v))
    

if __name__ == '__main__':
	main()
