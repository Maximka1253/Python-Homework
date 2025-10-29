n, m = map(int, input("Введите числа N >= 1 и M <= 100: ").split())
field = [input("Введите клетки поля, * - занятая клетка, . - пустая:").strip() for _ in range(n)]
count = 0
if 1 <= n or m <= 100:  
    for i in range(n):
        for j in range(m):
            if field[i][j] == '.':
                if i > 0 and field[i-1][j] != '.':
                    continue
                if i < n-1 and field[i+1][j] != '.':
                    continue
                if j > 0 and field[i][j-1] != '.':
                    continue
                if j < m-1 and field[i][j+1] != '.':
                    continue
                count += 1
    print("Корабль можно расположить ", count, " способами")
else:
    print("Неверные данные")