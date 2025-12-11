import heapq
def build_adj_list( V, edges):
    graph = {i: [] for i in range(V)}
    for u, v, wt in edges:
        graph[u].append((v, wt))
        graph[v].append((u, wt))
    return graph
def spanningTree( V, edges):
    # code here
    graph = build_adj_list(V, edges)

    visited = set()
    min_heap = [(0, 0)]  # (weight, node, parent)
    total_cost = 0

    while min_heap:
        wt, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += wt


        for adj, w in graph[node]:
            if adj not in visited:
                heapq.heappush(min_heap, (w, adj))

    return total_cost

V = 3
E = 3
Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
print(spanningTree(V, Edges))