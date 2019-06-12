graph = {
    'A' : ['B'],
    'B' : ['A','C','D'],
    'C' : ['B','D','E','G'],
    'D' : ['B','C','E','F'],
    'E' : ['C','D'],
    'F' : ['D'],
    'G' : ['C']
}
def dfs(graph:dict,s:str) -> None:
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while stack:
        temp = stack.pop()
        print(temp)
        w = graph[temp]
        for i in w:
            if i not in seen:
                stack.append(i)
                seen.add(i)
def dfs_rc(graph,s,seen=None):
    if seen == None: seen = set()
    print(s)
    seen.add(s)
    w = graph[s]
    for i in w:
        if i not in seen:
            dfs_rc(graph,i,seen)
#dfs(graph,'A')
dfs_rc(graph,'A')