
def get_unused_mb(used, allowance):
	leftover = allowance - used
	return leftover

	

def main():
    allowance = int(input())
    N = int(input())
    next_month = allowance
    i = 0
    while i < N:
    	used = int(input())
    	leftover = get_unused_mb(used,allowance)
    	next_month += leftover
    	i = i + 1
    print(next_month)
if __name__ == '__main__':
	main()
