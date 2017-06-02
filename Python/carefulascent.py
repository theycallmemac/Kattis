x, y = map(int, input().split())
n = int(input())

yd = 0
xd = 0

for i in range(n):
    start, end, factor = map(float, input().split())
    yd += end - start
    xd += (end - start) * factor

answer = (x * 1.0)/((y - tot_y_dist) + tot_x_dist)

print(answer)
