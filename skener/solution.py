
def main():

    r, c, zr, zc = map(int, input().split())
    lst = []
    
    for i in range(r):
      n = input()
      
        for j in range(zr):
          lst = [k * zc for k in n]
          print(''.join(lst))
          
if __name__ == '__main__':
    main()
