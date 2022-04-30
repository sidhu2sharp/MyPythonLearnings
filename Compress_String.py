lst = []
a, b = 0, 0
n = int(input())
for i in range(n):
    s = input()
    lst.append(s.split())
    a += int(lst[i][i])
    for j in range(n - 1, -1, -1):
        b += int(lst[i][j])
print(b)
#     lst.reverse()
# print(abs(a-b))
