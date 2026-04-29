class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #perfrom mutie BFS from all treasure cells at the same time
        #ditance on a never viisted land, skip visited and water
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = deque()

        #first put the treasure cell in q
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r, c) not in visited:
                    q.append((r,c))
                    visited.add((r,c))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        cur_distance = 0
        
        while q:
            #BFS level模板
            cur_lv_size = len(q)
            for _ in range(cur_lv_size):
                #we know all trasure cell are added, so all the pop are treasure cell
                #just need update its neibo one time, because each are definitely the closest
                cur = q.popleft()
                cur_r, cur_c = cur[0], cur[1]

                #check for valid neibos
                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc
                    #skip all in valid
                    if nr < 0 or nc <0 or nr == rows or nc == cols or grid[nr][nc] == -1 or (nr, nc) in visited:
                        continue
                    else:
                        #valid neibo fonnd, modify its content
                        #add distance for this level
                        # 关键点：邻居的距离 = 当前层的距离 + 1
                        grid[nr][nc] = cur_distance + 1
                        #add this to q for next level and mark visited
                        q.append((nr, nc))
                        visited.add((nr, nc))

            ## outside the loop：处理完这一层的所有节点后, for lensize循环finish ，距离才加 1        
            cur_distance += 1
                    



                    


        

        