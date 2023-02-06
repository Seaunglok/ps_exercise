E, S, M = map(int, input().split())
EN, SN, MN = 15, 28, 19
y = 1

while True:
    if (y-E) % EN == 0 and (y-S) % SN == 0 and (y-M) % MN == 0:
        break
    y += 1

print(y)