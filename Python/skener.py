
def main():

    Adrian = ('ABC' * 33) + 'A'
    Bruno = 'BABC' * 25
    Goran = ('CCAABB' * 16) + 'CCAA'

    counters = {'Adrian': 0,
                'Bruno': 0,
                'Goran': 0}

    qs = int(input().strip())
    ans = input().strip()

    for i in range(qs):
        if ans[i] is Adrian[i]:
            counters['Adrian'] += 1
        if ans[i] is Bruno[i]:
            counters['Bruno'] += 1
        if ans[i] is Goran[i]:
            counters['Goran'] += 1

    maxi = max(counters.values())

    print(maxi)

    for key in sorted(counters.keys()):
        if counters[key] is maxi:
            print(key)

if __name__ == '__main__':
    main()
