from collections import deque

class AnalisisGraf:
    def __init__(self, graf_dict):
        # Graf direpresentasikan sebagai dictionary
        self.graf = graf_dict

    def dfs(self, start_node):
        # Implementasi Depth-First Search (DFS)
        visited = set()
        stack = [start_node]
        hasil_penelusuran = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                hasil_penelusuran.append(node)
                # Tambahkan tetangga ke stack.
                tetangga = self.graf.get(node, [])
                stack.extend(reversed(tetangga))
        return hasil_penelusuran

    def bfs(self, start_node):
        #Implementasi Breadth-First Search (BFS)
        visited = set([start_node])
        queue = deque([start_node])
        hasil_penelusuran = []

        while queue:
            node = queue.popleft()
            hasil_penelusuran.append(node)
            for tetangga in self.graf.get(node, []):
                if tetangga not in visited:
                    visited.add(tetangga)
                    queue.append(tetangga)
        return hasil_penelusuran

    def ada_lintasan(self, node_a, node_b):
        # Menentukan apakah ada suatu lintasan dari a ke b
        if node_a not in self.graf or node_b not in self.graf:
            return False
        
        # Menggunakan BFS untuk mencari apakah b bisa dicapai dari a
        visited = set([node_a])
        queue = deque([node_a])

        while queue:
            sekarang = queue.popleft()
            if sekarang == node_b:
                return True # Lintasan ditemukan
            for tetangga in self.graf.get(sekarang, []):
                if tetangga not in visited:
                    visited.add(tetangga)
                    queue.append(tetangga)
        return False # Tidak ditemukan

    def cek_keterhubungan(self):
        # Menentukan keterhubungan graf (Connected Graph)
        if not self.graf:
            return True
        
        # Graf terhubung jika dari satu node acak, kita bisa mengunjungi SEMUA node lainnya
        node_awal = list(self.graf.keys())[0]
        node_terkunjungi = self.dfs(node_awal)
        
        # Jika jumlah node yang bisa dikunjungi sama dengan total node di graf, maka terhubung
        return len(node_terkunjungi) == len(self.graf)

if __name__ == "__main__":
    n = int(input("Banyak Node: "))
    m = int(input("Banyak Edge: "))

    graf = {}

    for i in range(1, n + 1):
        graf[i] = []

    print("Masukkan edge (format: u v)")
    for _ in range(m):
        u, v = map(int, input().split())
        graf[u].append(v)
        graf[v].append(u)

    program = AnalisisGraf(graf)

    A = int(input("Masukkan node A: "))
    B = int(input("Masukkan node B: "))

    print("\nDFS dari A:")
    dfsTraversal = program.dfs(A)
    print(*dfsTraversal)

    print("\nBFS dari A:")
    bfsTraversal = program.bfs(A)
    print(*bfsTraversal)

    print("\nAda lintasan dari A ke B? :", program.ada_lintasan(A, B))
    print("\nApakah graf terhubung penuh? :", program.cek_keterhubungan())
