class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        #visited and set for both ocean side

        pacific_visited = set()
        atlantic_visited = set()
        pacific_set = set()
        atlantic_set = set()

        #grab all the pacific and atlantic neibo cells
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific_set.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if r == rows - 1 or c == cols - 1:
                    atlantic_set.add((r,c))
        
        def dfs(r, c, visited):
            #base case
            if r < 0 or c < 0 or r == rows or c == cols:
                return
            
            if (r, c) in visited:
                return
            
            #add current valid cell in visited
            visited.add((r,c))

            #only dfs on valid nebios
            directions = [(1,0), (-1,0), (0,1),(0,-1)]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                #ignore invalid height cell
                #water only flow from higher equal height
                #so neibo cant be lower 
                if nr < 0 or nc < 0 or nr == rows or nc == cols:
                    continue
                if (nr, nc) in visited:
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                else:
                    dfs(nr, nc, visited)
        
            

        #peform dfs on each set to keep add valid neibo cells 
        #then collect the cells that in both set

        for r, c in pacific_set:
            dfs(r, c, pacific_visited)

        for r,c in atlantic_set:
            dfs(r, c, atlantic_visited)
        
        #你真正要比较的是：
        # pacific_visited
        # atlantic_visited
        # 因为它们才表示：
        # 哪些格子能流到 Pacific
        # 哪些格子能流到 Atlantic
        #find the same cells in both visited set
        result = []
        for cell in pacific_visited:
            if cell in atlantic_visited:
                result.append(cell)

        return result
        

        
