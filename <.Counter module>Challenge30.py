from collections import Counter
X = int(input())
N = Counter(map(int, input().split()))
c = int(input())

total = 0
for i in range(c):
  size, rate = map(int, input().split())
  if N[size]:
    N[size] -= 1
    total+= rate
print(total)   
