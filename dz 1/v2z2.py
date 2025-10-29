n = int(input())
passengers = []
for i in range(n):
    data = input().split()
    a = int(data[0])
    b = int(data[1])
    passengers.append((a, b))

T = int(input())

count = 0
for a, b in passengers:
    if a <= T <= b:
        count += 1

print(count)