class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0 # 修正：初始化为0，应对全水的情况
        cur_area = 0
        visited = set()

        def dfs(cur_r, cur_c):
            nonlocal cur_area

            #list down all basecases for a current block
            if cur_r < 0 or cur_c < 0 or cur_r == rows or cur_c == cols:
                return 
            
            if (cur_r, cur_c) in visited or grid[cur_r][cur_c] == 0:
                return 
            
            #now check this curent block
            
            #regardless of 0 or 1, we have visited this block
            visited.add((cur_r, cur_c))

            #now if this block is a land and never visited, increase area count
            if grid[cur_r][cur_c] == 1:
                cur_area += 1
            
            #dfs all neighbors
            dfs(cur_r + 1, cur_c)
            dfs(cur_r - 1, cur_c)
            dfs(cur_r, cur_c + 1)
            dfs(cur_r, cur_c - 1)

            #我们的目标是：“把整个岛扫一遍，只算一次”
            #没有撤销操作

        for row in range(rows):
            for col in range(cols):
                #start at an island and perform dfs for faster process
                if grid[row][col] == 1:
                    cur_area = 0   # 👈 每个岛重置
                    dfs(row, col)
                    #update the max area
                    max_area = max(max_area, cur_area)
        
        return max_area
                    