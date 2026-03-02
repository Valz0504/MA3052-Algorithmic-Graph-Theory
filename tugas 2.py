from collections import deque

class AnalisisGraf:
    def __init__(self, graf_dict):
        # Graf direpresentasikan sebagai dictionary
        self.graf = graf_dict

    def _dapatkan_semua_komponen(self):
        # Fungsi bantuan untuk mencari semua komponen yang terpisah
        visited = set()
        komponen_komponen = []

        for node in self.graf:
            if node not in visited:
                komponen_saat_ini = []
                queue = deque([node])
                visited.add(node)

                while queue:
                    curr = queue.popleft()
                    komponen_saat_ini.append(curr)
                    for tetangga in self.graf.get(curr, []):
                        if tetangga not in visited:
                            visited.add(tetangga)
                            queue.append(tetangga)
                
                komponen_komponen.append(komponen_saat_ini)
        return komponen_komponen

    def jumlah_komponen(self):
        # Menentukan jumlah komponen
        return len(self._dapatkan_semua_komponen())

    def komponen_terbesar(self):
        # Menentukan komponen terbesar
        komponen = self._dapatkan_semua_komponen()
        if not komponen:
            return []
        return max(komponen, key=len)

    def jumlah_island(self):
        # Menentukan jumlah island (sama dengan jumlah komponen)
        return self.jumlah_komponen()


if __name__ == "__main__":
    n = int(input("Banyak Node: "))
    m = int(input("Banyak Edge: "))

    graf = {}

    for i in range(1, n + 1):
        graf[i] = []

    print(f"Masukkan {m} edge (format: u v)")
    for _ in range(m):
        u, v = map(int, input().split())
        graf[u].append(v)
        graf[v].append(u) # Asumsi graf tidak berarah (undirected)

    program = AnalisisGraf(graf)

    print("\n================ HASIL ================")
    print("Jumlah komponen :", program.jumlah_komponen())
    print("Komponen terbesar :", *program.komponen_terbesar())
    print("Jumlah island :", program.jumlah_island())
    print("=======================================")
