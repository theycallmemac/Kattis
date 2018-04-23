from sys import stdin

def main():
  n = [i[::-1] for i in stdin.readline().strip().split()]
  print(sorted(n)[1])
if __name__ == '__main__':
    main()
