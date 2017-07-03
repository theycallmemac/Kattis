
def main():

    stones = str(input())

    whites = 0
    blacks = 0

    for stone in stones:
        if stone == "W":
            whites += 1
        else:
            blacks += 1

    if whites > blacks or blacks > whites:
        print("0")
    else:
        print("1")

if __name__ == '__main__':
    main()
