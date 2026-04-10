from collections import deque


def bfs(graph, start_node):
    # 1. 初始化队列，并将起点放入
    queue = deque([start_node])
    # 2. 初始化一个集合，记录已经访问过的节点，防止死循环
    visited = set([start_node])

    print("BFS 访问顺序: ", end="")

    # 3. 当队列不为空时，持续处理
    while queue:
        # 从队列头部拿出一个节点（先进先出 FIFO）
        current_node = queue.popleft()
        print(current_node, end=" -> ")

        # 4. 遍历该节点的所有邻居
        for neighbor in graph[current_node]:
            # 如果邻居没有被访问过
            if neighbor not in visited:
                visited.add(neighbor)  # 标记为已访问
                queue.append(neighbor)  # 将邻居加入队列尾部排队

# 这是一个示例图（可以想象成城市之间的连接）
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
# 运行测试
bfs(graph, 'A')
# 输出预期: A -> B -> C -> D -> E -> F ->