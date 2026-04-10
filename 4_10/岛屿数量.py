"""
题目描述： 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的
数量。岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
"""
"""
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
3
"""


def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        # 边界条件检查：
        # 1. 坐标越界
        # 2. 当前格子不是陆地 '1' (是水 '0' 或者已经访问过)
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return

        # 将当前陆地“沉没”（标记为 '0'）
        grid[r][c] = '0'

        # 向四个方向继续 DFS 扩散
        dfs(r + 1, c)  # 下
        dfs(r - 1, c)  # 上
        dfs(r, c + 1)  # 右
        dfs(r, c - 1)  # 左

    # 遍历整个网格
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                # 发现一个新岛屿，启动 DFS “沉岛”
                count += 1
                dfs(r, c)

    return count


# 测试数据
test_grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(f"岛屿总数: {numIslands(test_grid)}")  # 预期输出: 3