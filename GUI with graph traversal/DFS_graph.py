V, E = 6, 8
graph = [[] for _ in range(V)]
visited = [0 for _ in range(V)]
path = [-1 for _ in range(V)]

e1, e2 = [0, 0, 1, 1, 1, 2, 3, 3], [1, 3, 2, 3, 5, 5, 4, 5]

for i in range(E):
    graph[e1[i]].append(e2[i])
    graph[e2[i]].append(e1[i])


trace = list()


def DFS(s):
    for i in range(V):
        visited[i] = 0
        path[i] = -1
    trace.clear()

    l = []
    l.append(s)
    visited[s] = 1

    while len(l) > 0:
        u = l.pop()
        trace.append(str(u))

        for i in graph[u]:
            if visited[i] == 0:
                visited[i] = 1
                path[i] = u
                l.append(i)


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


# DFS(0)
# print(path)
# print(trace)
# print(trace)
# print(tracePath(0, 4))
# if __name__ == '__main__':

