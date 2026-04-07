graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C','D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}
# print( graph.keys())

def BFS(graph, s):
    queue = [s]

    while len(queue)>0:
         s = queue.pop(0)