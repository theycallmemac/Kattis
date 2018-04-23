from sys import stdin


def getNotTaken(taken,count,rooms):

  if taken == count:
      return "too late"
  else:
      return [j + 1 for j, roomtaken in enumerate(rooms) if not roomtaken][0]
      
      
def main():


    count, taken = (int(x) for x in stdin.readline().split())
    rooms = [False] * count
    
    for i in stdin.readlines():
        rooms[int(i) - 1] = True

    answer = getNotTaken(taken,count,rooms)
    print(answer)

if __name__ == '__main__':
    main()
