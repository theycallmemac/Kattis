from collections import defaultdict

def calculate(mapy,dicty):
    count = 0
    interesting_seq = 0
    for m in mapy:
        dicty[count] += 1
        count += m
        if count - 47 in dicty:
            interesting_seq += dicty[count-47]
    print(interesting_seq)
    return

def main():
    tests = int(input())
    for test in range(tests):
        input(), input()
        mapy = map(int, input().split())
        dicty = defaultdict(lambda: 0)
        calulate(mapy,dicty)
if __name__ == '__main__':
    main()
