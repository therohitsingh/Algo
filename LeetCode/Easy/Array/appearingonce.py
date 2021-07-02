from collections import defaultdict
data = defaultdict(list)

for _ in range(int(input())):
    name = input()
    score = float(input())
    data[score].append(name)

key = sorted(data)[1]
print(key)
print('\n'.join(sorted(data[key])))