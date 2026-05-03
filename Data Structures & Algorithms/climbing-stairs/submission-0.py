class Solution:
    def climbStairs(self, n: int) -> int:
        step_choices  = [1, 2]
        #n distance with these 2 step choices, if we top down we get
# n - 1       n -  2     #decsion we get
# -1.  -2.   -1.   -2.   This level repeats, use memo to cut duplicate
#invalid branches are the ones that return not 0 but < 0, means too much
        #递归 / DP 写之前，就想这 4 件事：
        ## 1. dp(state) 代表什么？
        #    这个节点要 return 给父节点什么答案？

        # 2. 最小成功 case 是什么？
        #    成功时应该贡献什么？

        # 3. 不合法 / 失败 case 是什么？
        #    失败时应该贡献什么？

        # 4. 父节点怎么合并子节点的答案？
        #    是加起来？取最大？取最小？or / and？
        distance = n
        memo = {}
        def dp(distance, step_choices):
            '''
            1. 每个子节点 return 的不是 path 本身，
               而是“从这个子节点开始，后面能贡献多少条合法走法”。

            2. distance == 0 时，说明当前这条分支刚好走到终点。
               这是一条完整合法 path，所以贡献 1。

            3. distance < 0 时，说明走过头了。
               这条分支非法，所以贡献 0。

            4. 这里不需要 backtrack 的 path.pop()，
               因为我们没有维护共享的 path list。
               每次只是把新的 distance 传给下一层函数，
               不会污染其他分支。

            5. 这题不会产生重复 path。
               因为一条从根到叶子的选择链，例如 [1, 2, 1]，
               只能由“先选 1，再选 2，再选 1”这一种方式生成。

            6. memo 不是用来去掉重复 path 的。
               memo 是用来避免重复计算相同子问题：
               比如 dp(2) 可能从不同前缀走到，但
               “还剩 2 阶有多少种走法”这个答案永远一样。
            '''

            #in memo, just return, stucked here
            if distance in memo:
                return memo[distance]

            #base case valid, reach end perfectly, return 1 to singal a path
            if distance == 0:
                return 1
            
            #invalid signal, cannot reach, contribute 0 path
            if distance < 0:
                return 0
            
            #initiliase the val contribute for current node choice
            curr_paths = 0

            #now lets go through the step choices, the branch
            for step_val in step_choices:
                remain_dist = distance - step_val
                #check subanswers
                sub_ans = dp(remain_dist, step_choices)
                #ignore any invalid
                if sub_ans == -100:
                    continue
                #get dp tree already unique from top, so get the answer
                curr_paths += sub_ans
            
            #save in memo
            memo[distance] = curr_paths
            #contribute to top
            return curr_paths

        return dp(distance, step_choices)

    
        