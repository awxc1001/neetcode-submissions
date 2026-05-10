class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #construct adj list
        n = numCourses
        adj = {i:[] for i in range(n)}
        #mapp the prequsites
        #he pair [0, 1], indicates that to take course 0 you have to first take course 1.
        #means node 1 origin to target node 0

        for preq in prerequisites:
            origin, target = preq[0], preq[1]
            adj[origin].append(target)
        
        #dfs + cycle detection on a run
        result = []
        #used for a single run of dfs to check if goes back to same node, visited is a global control
        cycle_set = set()
        visited = set()

        def dfs(node):

            if node in cycle_set:
                return False
            
            if node in visited:
                return True
            
            #check cycle to see if it valid)
            cycle_set.add(node)
            visited.add(node)
            for neibo in adj[node]:
                #if any cycle check failed, its incorrect and cannot compelte all lessons
                if dfs(neibo) == False:
                    return False
            cycle_set.remove(node)
            
            #pass cycle test add the node
            result.append(node)

            return True
        
        #same course might be sperate graph and standalone node, loop each course
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return result

        


    
        