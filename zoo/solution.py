def get_zoo(n, count):
    zoo = {}
    names = []
    i = 0
    while i < n:
        line = input().split()
        animal = line[-1].lower()
        if animal not in zoo:
            zoo[animal] = 1
            names.append(animal)
        else:
            zoo[animal] += 1
        i += 1
    names = sorted(names)
    zoolist = []
    for name in names:
         zoolist.append(f"{name} | {zoo[name]}")
    return zoolist

def main():
    n = int(input())
    count = 1
    output = []
    while n != 0:
        output.append(f"List {count}:")
        text = get_zoo(n, count)
        output += text
        n = int(input())
        count += 1
    for text in output:
        print(text)
if __name__ == "__main__":
    main()
