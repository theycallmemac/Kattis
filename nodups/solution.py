
def main():
    words = str(input()).split()
    seen =[]
    for i in words:
        if i not in seen:
            seen.append(i)
            output = "yes"
        else:
            output = "no"
            break
    print(output)

if __name__ == '__main__':
    main()

