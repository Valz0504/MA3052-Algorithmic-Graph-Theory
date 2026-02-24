from collections import deque

def dfs_rec(graph, visited, node, res):
    if visited[node]:
        return
    visited[node] = True
    res.append(node)
    for nxt in graph[node]:
        dfs_rec(graph, visited, nxt, res)

def dfs(graph, n, start_node):
    visited = [False] * (n + 1)
    res = []
    dfs_rec(graph, visited, start_node, res)
    return res

def bfs(graph, n, start_node):
    visited = [False] * (n + 1)
    res = []

    q = deque()
    visited[start_node] = True
    q.append(start_node)

    while q:
        curr = q.popleft()
        res.append(curr)

        for nxt in graph[curr]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

    return res

print("Banyak Node: ", end="")
n = int(input())

print("Banyak Edge: ", end="")
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print("Masukkan node A: ", end="")
A = int(input())

print("Masukkan node B: ", end="")
B = int(input())

print("Penelusuran menggunakan DFS dari A:", end=" ")
dfs_traversal = dfs(graph, n, A)
print(*dfs_traversal)

print("Penelusuran menggunakan BFS dari A:", end=" ")
bfs_traversal = bfs(graph, n, A)
print(*bfs_traversal)

# cek apakah ada lintasan dari A ke B
if B in dfs_traversal:
    print("ADA lintasan dari A ke B!")
else:
    print("TIDAK ADA lintasan dari A ke B!")

# cek apakah graph terhubung
if len(dfs_traversal) == n:
    print("Graf ini terhubung!")
else:
    print("Graf ini tidak terhubung!")