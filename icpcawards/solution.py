

def main():

    u, t, n = [], {}, int(input())
    for i in range(0, n):
        s, g = input().split()
        if s in u:
            pass
        else:
            u.append(s)
            t[s] = g
    for j in range(0, 12):
        print(u[j] + " " +  t[u[j]])

if __name__ == "__main__":
    main()
