class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.visited = set()
        self.count = 0

        start_r = 0
        start_c = 0
        #start from a point that is has "1", represent a land
        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == "1" and (r,c) not in self.visited:
                    #"1" means an island, add it and lets visit
                    self.count += 1

                    start_r = r
                    start_c = c
                    self.dfs(grid, rows, cols, start_r, start_c)
        
        return self.count
        
        
    
    def dfs(self, grid, rows, cols, r_i, c_i):
        #boundry check
        if (r_i < 0 or c_i < 0 or r_i == rows or c_i == cols):
            return
        
        # sea check and in visited check
        if (grid[r_i][c_i] == "0") or ((r_i, c_i) in self.visited):
            return
        
        #if path means an island, add location to visited as a tuple
        self.visited.add((r_i, c_i))

        #perfrom dfs on 4 directions
        self.dfs(grid, rows, cols, r_i + 1, c_i)
        self.dfs(grid, rows, cols, r_i - 1, c_i)
        self.dfs(grid, rows, cols, r_i, c_i + 1)
        self.dfs(grid, rows, cols, r_i, c_i - 1)
        

            
        


        