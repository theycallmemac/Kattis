from sys import stdin
read = stdin.readline()

dict = {}
for i in read:
    i = i.strip().split()
    if i[0].isdigit():
        dict[int(i[0])//2] = i[1]
    else:
        dict[int(i[1])] = i[0]
        
for radius, colour in sorted(dict.items()):
  print(colour) 
