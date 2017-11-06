def main():
    num_gnomes = int(input())

    i = 0
    while i < num_gnomes:
        group = str(input()).split(" ")
        g = group[0]
        group = group[1:]
        maxi_pos = 0
        j = 0
        while j < len(group):
            if (int(group[j]) + 1) == (int(group[j + 1])):
                pass
            if (int(group[j]) - 1) == (int(group[j + 1])):
                pass
            else:
                maxi_pos = j + 2
            j += 1
        print(maxi_pos)
        i += 1

if __name__ == '__main__':
    main()
