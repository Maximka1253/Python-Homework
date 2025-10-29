n = int(input())
board = [[0] * 8 for _ in range(8)]
for _ in range(n):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1
perimeter = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == 1:
            if i == 0 or board[i-1][j] == 0:
                perimeter += 1
            if i == 7 or board[i+1][j] == 0:
                perimeter += 1
            if j == 0 or board[i][j-1] == 0:
                perimeter += 1
            if j == 7 or board[i][j+1] == 0:
                perimeter += 1
print(perimeter)