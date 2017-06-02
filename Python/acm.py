dict = {}
other = {}


while True:
    in = input().split()

    if len(in) == 1:
        break
    t = int(in[0])

    x = in[1]
    
    if x in dict:
        continue
        
    if x in other:
        other[x] += 1
    else:
        other[x] = 1
        
    if in[2] == 'right':
        dict[x] = t

print(len(dict), end=' ')
print(sum([dict[i] + 20*(other[i]-1) for i in dict])) 
