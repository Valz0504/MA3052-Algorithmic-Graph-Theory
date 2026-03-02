from collections import deque

class AnalisisGraf:
    def __init__(self, graf_dict):
        self.graf = graf_dict

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        hasil = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                hasil.append(node)
                stack.extend(reversed(self.graf.get(node, [])))
        return hasil

    def bfs(self, start_node):
        visited = set([start_node])
        queue = deque([start_node])
        hasil = []

        while queue:
            node = queue.popleft()
            hasil.append(node)
            for tetangga in self.graf.get(node, []):
                if tetangga not in visited:
                    visited.add(tetangga)
                    queue.append(tetangga)
        return hasil

    def ada_lintasan(self, node_a, node_b):
        if node_a not in self.graf or node_b not in self.graf:
            return False
        visited = set([node_a])
        queue = deque([node_a])
        while queue:
            sekarang = queue.popleft()
            if sekarang == node_b:
                return True
            for tetangga in self.graf.get(sekarang, []):
                if tetangga not in visited:
                    visited.add(tetangga)
                    queue.append(tetangga)
        return False

    def cek_keterhubungan(self):
        if not self.graf:
            return True
        node_awal = list(self.graf.keys())[0]
        node_terkunjungi = self.dfs(node_awal)
        return len(node_terkunjungi) == len(self.graf)

    def cari_komponen(self):
        visited = set()
        jumlah_komponen = 0
        komponen_terbesar = []

        for node in self.graf:
            if node not in visited:
                jumlah_komponen += 1
                hasil = self.dfs(node)
                visited.update(hasil)
                if len(hasil) > len(komponen_terbesar):
                    komponen_terbesar = hasil

        return jumlah_komponen, komponen_terbesar


def hitung_island(grid, baris, kolom):
    visited = [[False] * (kolom + 1) for _ in range(baris + 1)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0

    for i in range(1, baris + 1):
        for j in range(1, kolom + 1):
            if visited[i][j] or grid[i][j] == 0:
                continue

            cnt += 1
            visited[i][j] = True
            queue = deque([(i, j)])

            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 1 <= nx <= baris and 1 <= ny <= kolom and not visited[nx][ny] and grid[nx][ny] != 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

    return cnt


def baca_graf():
    n = int(input("Banyak Node: "))
    m = int(input("Banyak Edge: "))
    graf = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graf[u].append(v)
        graf[v].append(u)
    return graf, n


if __name__ == "__main__":
    print("Pilih menu yang ingin diakses:")
    print("1. Penelusuran DFS")
    print("2. Penelusuran BFS")
    print("3. Cek Keberadaan Lintasan")
    print("4. Cek Keterhubungan Graf")
    print("5. Cari jumlah komponen dan komponen terbesar")
    print("6. Cari jumlah island")
    print("7. Exit")

    tipe = int(input())

    if tipe == 7:
        exit()

    if tipe == 6:
        baris = int(input("Masukkan jumlah baris: "))
        kolom = int(input("Masukkan jumlah kolom: "))
        grid = [[0] * (kolom + 1) for _ in range(baris + 1)]
        for i in range(1, baris + 1):
            vals = list(map(int, input().split()))
            for j in range(kolom):
                grid[i][j + 1] = vals[j]
        print(f"Jumlah island: {hitung_island(grid, baris, kolom)}")
    else:
        graf, n = baca_graf()
        program = AnalisisGraf(graf)

        if tipe == 1:
            A = int(input("Masukkan node A: "))
            print("\nPenelusuran menggunakan DFS dari A:", *program.dfs(A))

        elif tipe == 2:
            A = int(input("Masukkan node A: "))
            print("\nPenelusuran menggunakan BFS dari A:", *program.bfs(A))

        elif tipe == 3:
            A = int(input("Masukkan node A: "))
            B = int(input("Masukkan node B: "))
            if program.ada_lintasan(A, B):
                print("\nADA lintasan dari A ke B!")
            else:
                print("\nTIDAK ADA lintasan dari A ke B!")

        elif tipe == 4:
            if program.cek_keterhubungan():
                print("\nGraf ini terhubung!")
            else:
                print("\nGraf ini tidak terhubung!")

        elif tipe == 5:
            jumlah, terbesar = program.cari_komponen()
            print(f"\nJumlah component: {jumlah}")
            print("Component terbesar berada di node-node berikut:", *terbesar)
