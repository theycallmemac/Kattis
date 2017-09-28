def get_answer(total, n):
    for i in range(0, n):
        if "CD" not in input().strip():
            total = total + 1
    return total

def main():
    n = int(input())
    total = 0
    answer = get_answer(total, n)
    print(answer)
if __name__ == '__main__':
    main()


