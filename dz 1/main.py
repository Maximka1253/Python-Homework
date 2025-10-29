list = [int(i) for i in input().split()]
unic = []
for i in list:
    if list.count(i) > 1:
        unic.append(i)
print(sorted(set(unic)))