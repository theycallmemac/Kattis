import sys
def main():
  cases = int(stdin.readline().strip())
  case = 1

  for i in range(cases):
      rows, columns = stdin.readline().strip().split()
      rows = int(rows)
      columns = int(columns)
      lst = []
      print("Test", case)
      for i in range(rows):
          lst.append(list(stdin.readline().strip()))  
      case += 1
      lst = reversed(lst)   
      for item in lst:
        print("".join(reversed(item)))
if __name__ == '__main__':
    main()
