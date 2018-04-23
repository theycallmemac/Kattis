from itertools import combinations
from sys import stdin


def find_dwarf_sum(numbers, target):
    results = []
    for i in range(len(numbers)):
        results.extend([combination for combination in combinations(numbers ,i) if sum(combination) == target])

    for result in results:
        if len(result) == 7:
            return list(result)
    return 0

def main():
    numbers = []
    i = 0
    while i < 9:
        n = int(input())
        numbers.append(n)
        i += 1
    results = find_dwarf_sum(numbers, 100)

    answer = []
    i = 0
    while i < len(numbers):
        j = 0
        while j < len(results):
            if results[j] == numbers[i]:
                answer.append(results[j])
            j += 1
        i += 1
    [print(i) for i in answer]



if __name__ == '__main__':
    main()
