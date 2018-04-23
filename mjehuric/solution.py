def main():
    lst = [int(i) for i in input().split()]
    while (lst != [1,2,3,4,5]):
        for j in range(4):
            if lst[j] > lst[j+1]:
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp
                print(" ".join([str(k) for k in lst]))
if __name__ == '__main__':
    main()
