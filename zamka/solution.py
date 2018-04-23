from sys import stdin

def main():
  low = int(stdin.readline().strip())
  high = int(stdin.readline().strip())
  total = int(stdin.readline().strip())

  for i in range(low, high+1):
    
      lst = list(str(i))
      if sum([int(j) for j in lst]) == total:
          print(i)
          break

  for k in range(high, low-1, -1):
      lst = list(str(k))
      if sum([int(j) for j in lst]) == total:
          print(k)
          break
if __name__ == '__main__':
    main()
