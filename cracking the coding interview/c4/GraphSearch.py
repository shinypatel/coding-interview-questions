n = 4
adj_mat = [[0, 1, 1, 0],
           [0, 0, 0, 1],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]
visited = [0 for i in range(n)]

queue = []


def dfs(i):
    visited[i] = 1
    print(i)
    for j in range(n):
        if adj_mat[i][j] and not visited[j]:
            dfs(j)


def run_dfs():  # q2
    for i in range(n):
        if not visited[i]:
            dfs(i)


def bfs(i):
    visited[i] = 1
    print(i)
    for j in range(n):
        if adj_mat[i][j] and not visited[j]:
            queue.append(j)
    if queue:
        bfs(queue.pop(0))


def run_bfs():
    for i in range(n):
        if not visited[i]:
            bfs(i)


run_dfs()
# run_bfs()
