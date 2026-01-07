import sys
import heapq

def neighbors(r, c, heights, N, M):
    """Генератор соседних клеток, удовлетворяющих условию по высоте."""
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and abs(heights[r][c] - heights[nr][nc]) <= 100:
            yield nr, nc

def dijkstra(source, target, heights, N, M):
    """Алгоритм Дейкстры для поиска кратчайшего пути."""
    dist = [[float('inf')] * M for _ in range(N)]
    sr, sc = source
    dist[sr][sc] = 0
    pq = [(0, sr, sc)]  # (расстояние, строка, столбец)
    while pq:
        d, r, c = heapq.heappop(pq)
        if (r, c) == target:
            return d
        if d > dist[r][c]:
            continue
        for nr, nc in neighbors(r, c, heights, N, M):
            if dist[r][c] + 1 < dist[nr][nc]:
                dist[nr][nc] = dist[r][c] + 1
                heapq.heappush(pq, (dist[nr][nc], nr, nc))
    return float('inf')  # если путь не найден (по условию гарантируется)

def manhattan(a, b):
    """Манхэттенское расстояние между двумя клетками."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(source, target, heights, N, M):
    """Алгоритм A* для поиска кратчайшего пути с эвристикой Манхэттена."""
    g = [[float('inf')] * M for _ in range(N)]  # стоимость от начала до текущей клетки
    sr, sc = source
    g[sr][sc] = 0
    h_start = manhattan(source, target)
    pq = [(h_start, sr, sc)]  # (f = g + h, строка, столбец)
    while pq:
        f, r, c = heapq.heappop(pq)
        if (r, c) == target:
            return g[r][c]
        # Проверка на устаревшие записи в очереди
        if f > g[r][c] + manhattan((r, c), target):
            continue
        for nr, nc in neighbors(r, c, heights, N, M):
            tentative_g = g[r][c] + 1
            if tentative_g < g[nr][nc]:
                g[nr][nc] = tentative_g
                f_new = tentative_g + manhattan((nr, nc), target)
                heapq.heappush(pq, (f_new, nr, nc))
    return float('inf')  # если путь не найден (по условию гарантируется)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    heights = [[int(next(it)) for _ in range(M)] for _ in range(N)]
    start = (int(next(it)), int(next(it)))
    cargo = (int(next(it)), int(next(it)))
    dest = (int(next(it)), int(next(it)))

    # Используем алгоритм Дейкстры
    dist1_dijkstra = dijkstra(start, cargo, heights, N, M)
    dist2_dijkstra = dijkstra(cargo, dest, heights, N, M)
    total_dijkstra = dist1_dijkstra + dist2_dijkstra

    # Используем алгоритм A*
    dist1_astar = astar(start, cargo, heights, N, M)
    dist2_astar = astar(cargo, dest, heights, N, M)
    total_astar = dist1_astar + dist2_astar

    # Результаты должны совпадать
    assert total_dijkstra == total_astar, "Результаты алгоритмов различаются"
    print(total_dijkstra)

if __name__ == "__main__":
    main()