import re


for i in range(int(input())):
    s = input()
    if (bool(re.match(r'^[7-9]', s)) and s.isdigit() and len(s) == 10):
            print('YES')
    else:
        print("NO")
