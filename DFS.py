def dfs_recursive(graph, current_node, visited=None):
    # 初始化 visited 集合（仅在第一次调用时初始化）
    if visited is None:
        visited = set()
        print("DFS(递归) 访问顺序: ", end="")

    # 1. 将当前节点标记为已访问
    visited.add(current_node)
    print(current_node, end=" -> ")

    # 2. 遍历当前节点的所有邻居
    for neighbor in graph[current_node]:
        # 3. 如果邻居没被访问过，直接"深入"（递归调用）
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# 运行测试
# 这是一个示例图（可以想象成城市之间的连接）
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
dfs_recursive(graph, 'A')
# 输出预期: A -> B -> D -> E -> F -> C ->