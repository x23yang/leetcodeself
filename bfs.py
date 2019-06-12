graph = {
    'A' : ['B','C'],
    'B' : ['A','C','D'],
    'C' : ['A','B','D','E'],
    'D' : ['B','C','E','F'],
    'E' : ['C','D'],
    'F' : ['D']
}
def bfs(graph,s):
    queue = []
    queue.append(s)
    seen=set()
    seen.add(s)
    while queue:
        temp = queue.pop(0)
        print(temp)
        w = graph[temp]
        for i in w:
            if i not in seen:
                queue.append(i)
                seen.add(i)
bfs(graph,'B')
