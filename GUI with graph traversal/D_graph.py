import queue

V, E = 6, 10
graph = [[] for _ in range(V)]
path = [-1 for _ in range(V)]
dist = [1e9 for _ in range(V)]

e1 = [0, 1, 1, 1, 2, 3, 3, 3, 4, 5]
e2 = [(1, 1), (2, 5), (3, 2), (5, 7), (5, 1),
      (0, 2), (2, 1), (4, 4), (3, 3), (4, 1)]


class Node:
    def __init__(self, val, weight):
        self.val = val
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f'({self.val}, {self.weight})'


for i in range(E):
    graph[e1[i]].append(Node(e2[i][0], e2[i][1]))

trace = []


def Dijkstra(s):
    for i in range(V):
        dist[i] = 1e9
        path[i] = -1
    trace.clear()

    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0

    while not pq.empty():
        u = pq.get()
        trace.append(str(u.val))

        for v in graph[u.val]:
            if dist[u.val] + v.weight < dist[v.val]:
                dist[v.val] = dist[u.val] + v.weight
                path[v.val] = u.val
                pq.put(Node(v.val, dist[v.val]))
                

def tracePath(s, f):
    b = []

    if s == f:
        return str(s)

    if path[f] == -1:
        return f'No path!'

    while s != f:
        b.append(f)
        f = path[f]

    b.append(f)
    return '->'.join(map(str, reversed(b)))


# Dijkstra(0)
# trace = ' '.join(map(str, trace))
# print(tracePath(0, 5))
