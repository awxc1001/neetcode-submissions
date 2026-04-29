class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = deque()

        #当前代码有问题，下面的bfs就算全是烂也会at least跑一次bfs，导致return多一分钟，cannot return -1
        #to fix, use a fresh count
        fresh_count = 0

        #first loop all cells in the grid once to add all rotten fruit cells in q
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rot_tuple = (r, c)
                    q.append(rot_tuple)
                    visited.add(rot_tuple)
                    
                #use fresh_count to stop bfs immedaitely going to next level if all are rotten
                elif grid[r][c] == 1:
                    fresh_count += 1

        #no time needed if all are rot fruit            
        if fresh_count == 0:
            return 0
        
        #now we perform multi source bfs, first level in q are all rotten fruits
        #Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        cur_min = 0

        while q and fresh_count > 0: # 只要没有新鲜橘子了，就立刻停止，防止多算一分钟:
            level_size = len(q)
            for _ in range(level_size):
                #same time level nodes
                cur_r, cur_c = q.popleft()
                #check the choices of this node
                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc
                    #skip visited and empty cells and those not in grid constraints
                    if nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in visited or grid[nr][nc] == 0:
                        continue
                    else:
                        #this is a never visited fresh fruit cell
                        #rot it and add the que as a valid nebos, also mark visted
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        # 新鲜橘子少了一个
                        fresh_count -= 1

            #outside loop, one level finish, increment minute
            cur_min += 1
        
        #loop stops when everything visited and no fresh, no more to add in q
        ## 最后检查：如果新鲜橘子没被消灭完，说明有孤儿橘子，返回 -1
        return cur_min if fresh_count == 0 else -1
        






                

        