class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #course dependency map for all courses. 
        #Even courses with no prerequisites need to be in the map 
        #(they just point to an empty list, meaning "ready to take").
        #有些course没有preq说明这个图有可能部分节点不连在一起，会有独立的sub graph

        #There are a total of numCourses courses you are required to take, 
        #labeled from 0 to numCourses - 1.

        #make the adj mapping template
        course_map = {course_label:[] for course_label in range(numCourses)}

        #build up the adj list graph
        #[0, 1], indicates that must take course 1 before taking course 0
        #so from [1] to [0]
        for course, preq in prerequisites:
            #course_map[preq] = course  # ❌ This overwrites! Should append to a list
            course_map[preq].append(course)
        
        #now dfs to check if there is a cycle
        #we use two seperate hashset
        #记录已经彻底检查完、确认没问题的点。
        #这样以后再遇到它，可以直接跳过，提高效率。
        visited = set()

        #记录当前这条 DFS 路径上有哪些点。
        #如果在当前路径里又走回来了，说明出现环。
        curr_dfs_path = set()

        def dfs(course): #return True if found a cycle
            #since adj list, no boundry check base case
            #if this node was in dfs_path_already then cycle is detected
            if course in curr_dfs_path:
                return True
            
            if course in visited:
                return False
            
            #curr node operation
            curr_dfs_path.add(course)
            visited.add(course)

            #dfs from its neibos
            for neibo in course_map[course]:
                #if any cycle detected
                if dfs(neibo):
                    return True
                #排列题backtracking 是在for loop里面加入和撤销
                # “我选了一个数字进路径”
                # 所以递归回来后撤销这个数字
                # 这题
                # “我进入了一个节点，当前递归栈里有它”
                # 所以等这个节点的c所有后续都查完，再把它移出递归栈
            #撤销time要和add的time相对应
            #也就是说，reset 要和“add 当前节点”成对出现，而不是和 for 里的某个邻居成对出现。
            curr_dfs_path.remove(course)

        #check each point on the map, since all
        #can be disconnected node subgraph
        for course in course_map:
            #cycle detected, cannot complete all courses
            if dfs(course):
                return False

        #True for course can complete
        return True





        