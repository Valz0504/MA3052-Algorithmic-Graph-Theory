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

# CONTOH PENGGUNAAN 1

if __name__ == "__main__":
    # Membuat graf contoh (Undirected Graph). 
    contoh_graf = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B'],
        'D': ['E'],
        'E': ['D'],
        'F': []
    }

    program = AnalisisGraf(contoh_graf)

    print("--- HASIL TUGAS 1 ---")
    print(f"1. DFS dari 'A': {program.dfs('A')}")
    print(f"2. BFS dari 'A': {program.bfs('A')}")
    print(f"3. Ada lintasan 'A' ke 'C'? : {program.ada_lintasan('A', 'C')}")
    print(f"4. Ada lintasan 'A' ke 'E'? : {program.ada_lintasan('A', 'E')}")
    print(f"5. Apakah graf terhubung penuh? : {program.cek_keterhubungan()}")

  # CONTOH PENGGUNAAN 2

if __name__ == "__main__":
    # Membuat graf contoh (Undirected Graph). 
    contoh_graf = {
        'A': ['B', 'C', 'E'],
        'B': ['B', 'C'],
        'C': ['A', 'B'],
        'D': ['E', 'F'],
        'E': ['A', 'D'],
        'F': ['D']
    }

    program = AnalisisGraf(contoh_graf)

    print("--- HASIL TUGAS 1 ---")
    print(f"1. DFS dari 'A': {program.dfs('A')}")
    print(f"2. BFS dari 'A': {program.bfs('A')}")
    print(f"3. Ada lintasan 'A' ke 'C'? : {program.ada_lintasan('A', 'C')}")
    print(f"4. Ada lintasan 'A' ke 'E'? : {program.ada_lintasan('A', 'E')}")
    print(f"5. Apakah graf terhubung penuh? : {program.cek_keterhubungan()}")
