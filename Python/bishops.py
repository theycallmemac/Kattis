import sys

def get_bishops(board_size):
    if int(board_size) == 1:
        return(1)
    else:
        return (int(board_size) * 2 - 2)

def main():
    lines = sys.stdin
    for line in lines:
        print(get_bishops(line))
if __name__ == '__main__':
	main()
