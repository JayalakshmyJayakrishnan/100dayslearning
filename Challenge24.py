n = int(input())                          
stamps = set()

for i in range(n):
    country = input().strip()
    stamps.add(country)
print(len(stamps))   

