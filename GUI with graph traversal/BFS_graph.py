import queue

V, E = 6, 8
graph = [[] for _ in range(V)]
visited = [0 for _ in range(V)]
path = [-1 for _ in range(V)]

e1, e2 = [0, 0, 1, 1, 1, 2, 3, 3], [1, 3, 2, 3, 5, 5, 4, 5]

for i in range(E):
    graph[e1[i]].append(e2[i])
    graph[e2[i]].append(e1[i])


trace = list()


def BFS(s):
    for i in range(V):
        visited[i] = 0
        path[i] = -1
    trace.clear()

    q = queue.Queue()
    q.put(s)
    visited[s] = 1

    while not q.empty():
        u = q.get()
        trace.append(str(u))

        for i in graph[u]:
            if visited[i] == 0:
                visited[i] = 1
                path[i] = u
                q.put(i)


def tracePath(s, f):
    b = []

    if s == f:
        return str(f)

    if path[f] == -1:
        return f'No path!'

    while s != f:
        b.append(f)
        f = path[f]

    b.append(f)
    return '->'.join(map(str, reversed(b)))


# BFS(0)
# trace = ' '.join(trace)
# print(trace)
# print(tracePath(0, 4))
