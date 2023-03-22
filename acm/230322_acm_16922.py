from itertools import combinations_with_replacement

N = int(input())
sol = set()
number = [1, 5, 10, 50]

for i in combinations_with_replacement(number, N):
    sol.add(sum(i))
    
print(len(sol))




