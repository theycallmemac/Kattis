from sys import stdin
from math import ceil

def main():
  cals = 400

  _ = stdin.readline()

  for n in stdin:
      n = int(n.strip())
    print(ceil(n / cals))
    
if __name__ == '__main__':
    main()
