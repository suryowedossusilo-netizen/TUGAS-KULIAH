from collections import deque

class EdmondsKarp:
    def __init__(self, graph, source, sink):
        self.graph = graph
        self.source = source
        self.sink = sink
        self.flow = {}
        self.residual = {}
        self.iterations = 0
        self.paths_found = []
        
        all_nodes = set(graph.keys())
        for u in graph:
            for v in graph[u]:
                all_nodes.add(v)
        
        for node in all_nodes:
            self.residual[node] = {}
        
        for u in graph:
            for v in graph[u]:
                self.residual[u][v] = graph[u][v]
                self.flow[(u, v)] = 0
                if u not in self.residual[v]:
                    self.residual[v][u] = 0
    
    def bfs(self):
        parent = {self.source: None}
        queue = deque([self.source])
        
        while queue:
            u = queue.popleft()
            for v in self.residual[u]:
                if v not in parent and self.residual[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
                    if v == self.sink:
                        return parent
        return None
    
    def get_path_capacity(self, parent):
        path = []
        v = self.sink
        while v != self.source:
            u = parent[v]
            path.append((u, v))
            v = u
        path.reverse()
        min_cap = min(self.residual[u][v] for u, v in path)
        return path, min_cap
    
    def augment_flow(self, path, flow_amount):
        for u, v in path:
            self.residual[u][v] -= flow_amount
            self.residual[v][u] += flow_amount
            if (u, v) in self.flow:
                self.flow[(u, v)] += flow_amount
            else:
                self.flow[(v, u)] -= flow_amount
    
    def max_flow(self):
        total_flow = 0
        
        print("=" * 60)
        print("  ALGORITMA EDMONDS-KARP (1972) - VERSI MURNI")
        print("=" * 60)
        
        while True:
            parent = self.bfs()
            if parent is None:
                break
            
            path, path_flow = self.get_path_capacity(parent)
            self.augment_flow(path, path_flow)
            total_flow += path_flow
            self.iterations += 1
            
            path_str = " -> ".join([str(p[0]) for p in path] + [str(self.sink)])
            self.paths_found.append({
                'path': path,
                'path_str': path_str,
                'flow': path_flow
            })
            
            print(f"  Iterasi {self.iterations}: Path {path_str}, Aliran = {path_flow} L/s")
        
        print(f"\n{'=' * 60}")
        print(f"  ALIRAN MAKSIMUM = {total_flow} L/s")
        print(f"  JUMLAH ITERASI = {self.iterations}")
        print(f"{'=' * 60}")
        
        return total_flow


def create_network_8():
    return {
        's': {'A': 100, 'B': 80},
        'A': {'C': 70, 'D': 50},
        'B': {'C': 60, 'D': 40},
        'C': {'t': 90},
        'D': {'t': 70},
        't': {}
    }


# ========== MAIN ==========
print("\n" + "=" * 70)
print("  IMPLEMENTASI ALGORITMA EDMONDS-KARP (VERSI MURNI)")
print("  Optimasi Jaringan Distribusi Air PDAM")
print("=" * 70)

graph = create_network_8()

print("\n  Struktur Jaringan (8 Titik):")
print("  " + "-" * 50)
for u in sorted(graph.keys()):
    edges = [f"{v}({graph[u][v]})" for v in graph[u] if graph[u][v] > 0]
    if edges:
        print(f"  {u:<8} -->  {', '.join(edges)}")

algo = EdmondsKarp(graph, 's', 't')
max_flow = algo.max_flow()

print("\n" + "=" * 60)
print("  DISTRIBUSI ALIRAN PER SISI:")
print("  " + "-" * 56)
for (u, v), flow_val in sorted(algo.flow.items()):
    cap = graph[u].get(v, 0)
    if cap > 0:
        pct = (flow_val / cap) * 100
        print(f"  {u}->{v:<8} {flow_val:>6.0f}/{cap:<6.0f} ({pct:>5.1f}%)")

print("\n" + "=" * 60)
print("  PATH AUGMENTING YANG DITEMUKAN:")
print("  " + "-" * 56)
for i, p in enumerate(algo.paths_found, 1):
    print(f"  Iterasi {i}: {p['path_str']:<20} Aliran = {p['flow']} L/s")

print("\n" + "=" * 70)
print("  PROGRAM SELESAI!")
print("=" * 70 + "\n")