from sys import stdin

lst = stdin.readline().strip()
lst = list(seq)
s = lst.pop(0)

u = 0
d = 0
p = 0
          
if s == "U" and lst[0] == "U":
    d += 1
if s == "U" and lst[0] == "D":
    u += 2
    d += 1
    p += 1
if s == "D" and lst[0] == "D":
    u += 1  
if start == "D" and lst[0] == "U":
    u += 1
    d += 2
    p += 1

j = lst[0]

if len(lst) > 1: 
    for i in lst[1:]:
        if i == "D":
            u += 2 
        else:
            d += 2
        if i != j:
            p += 1
            j = i

print(str(u) + "\n" + str(d) + "\n" + str(p))
