from collections import Counter

n = int(input())
s = input()
lst = s.split()
lst.sort()
a = sorted(Counter(lst).items(), key=lambda x: x[1], reverse=True)
print(a[0][0])
