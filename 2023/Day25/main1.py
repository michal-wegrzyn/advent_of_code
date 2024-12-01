import sys
from collections import deque

lines = [[line.split(': ')[0], line.split(': ')[1].split(' ')] for line in open('input.txt').read().strip().split('\n')]
graph = {}
edges_cnt = 0
edges = []
vertex = ''
for k, v in lines:
    if not k in graph:
        graph[k] = []
        vertex = k
    for i in v:
        if not i in graph:
            graph[i] = []
        graph[i].append((k, edges_cnt))
        graph[k].append((i,edges_cnt))
        edges.append((k,i))
        edges_cnt += 1

sys.setrecursionlimit(len(graph)*2)

def find_bridge(deleted):
    data = {}
    data['visited'] = {k:0 for k in graph.keys()}
    data['low'] = {k:0 for k in graph.keys()}
    data['preorder'] = {k:0 for k in graph.keys()}
    data['time'] = 0
    data['deleted'] = deleted
    bridge = dfs(vertex, None, data)
    return bridge

def dfs(v, p, data):
    data['visited'][v] = 1
    data['time'] += 1
    data['low'][v] = data['time']
    data['preorder'][v] = data['time']
    for u, ind in graph[v]:
        # print(v, u, ind)
        if ind in data['deleted']:
            continue
        if data['visited'][u] == 0:
            rec = dfs(u, v, data)
            if not rec is None:
                return rec
            data['low'][v] = min(data['low'][v], data['low'][u])
            if data['low'][u] > data['preorder'][v]:
                return ind
        elif u != p:
            # print(data['low'])
            data['low'][v] = min(data['low'][v], data['preorder'][u])
    return None

def size(v, deleted):
    vertices = [v]
    ind = 0
    while ind < len(vertices):
        for u, edge in graph[vertices[ind]]:
            if u in vertices:
                continue
            if edge in deleted:
                continue
            vertices.append(u)
        ind += 1

    return len(vertices)

def shortest_path(start, end, deleted):
    edge = {k:(-1,-1) for k in graph.keys()}
    edge[start] = (-2,-2)
    process = deque()
    process.append(start)
    while len(process):
        v = process.popleft()
        # print(v)
        for u, ind in graph[v]:
            if ind == deleted:
                continue
            if edge[u] != (-1,-1):
                continue
            edge[u] = (v, ind)
            process.append(u)
        if edge[end] != (-1,-1):
            break
    res = []
    curr = edge[end]
    while curr != (-2,-2):
        # print(curr)
        res.append(curr[1])
        curr = edge[curr[0]]
    return res

bridge = None
deleted = ()
print(edges_cnt)
for e1 in range(edges_cnt):
    p = shortest_path(edges[e1][0], edges[e1][1], e1)
    # print(p)
    if e1%100 == 0:
        print(e1)
    if not bridge is None:
        break
    for e2 in p:
        if not bridge is None:
            break
        deleted = (e1,e2)
        bridge = find_bridge(deleted)
        deleted = (e1,e2,bridge)

s = size(vertex, deleted)
ans = s*(len(graph)-s)
print(ans)