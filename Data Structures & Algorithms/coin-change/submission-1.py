class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            #amount. 3 coin choices , each level one pick one coin
    #a - c1       a - c2      a -c3
   #-c1 -c2 -c3
   #same for every change, reduce duplicate branch and remove any that amount gives < 0        

        # --- 第一段：建立账本 (Memoization) ---
        # 记录算过的 amount，防止重复走进相同的分支 (reduce duplicate branch)
        memo = {}

        def dp(coins, amount):


            # --- 第三段：设定终点与死路 (Base Cases) ---
            # 情况 A: 恰好凑齐了，剩下的钱需要 0 枚硬币
            if amount == 0:
                return 0
            # 情况 B: 凑过头了，返回 -100 表示这条路走不通 (信号旗)
            if amount < 0:
                return -100
            
                        # --- 第二段：检查账本 (Lookup) ---
            # 如果之前算过这个金额，直接把结果拿出来，不再往下递归
            if amount in memo:
                return memo[amount]
            # --- 第四段：多叉树探索与货比三家 (Core Competition) ---
            # 初始化当前金额的“子问题最强王者”为无穷大
            smallest_sub_answer = math.inf

            # 遍历每一种硬币选择，看看哪条分支回来的答案最给力
            for coin_val in coins:
                # 派出一个递归分身，去问剩下的钱最少要几枚
                remain_amount = amount - coin_val
                sub_answer = dp(coins, remain_amount)

                # 【剪枝】：如果子问题反馈是死路 (-100)，直接跳过
                if sub_answer == -100:
                    continue
                
                # 【关键】：这里只比大小，不加 1
                # 目标是：在所有能走通的分支里，找出那个用硬币最少的
                smallest_sub_answer = min(smallest_sub_answer, sub_answer)

            # --- 第五段：收网总结与加冕 (Post-processing & Reporting) ---
            
            # 如果所有的树枝都走不通（依然是初始的 inf）
            if smallest_sub_answer == math.inf:
                # 那么当前这个 amount 也是死路，给自己贴上 -100 标签
                res = -100
            else:
                # 【拿到了再操作】：挑出了最好的子答案，现在加上自己捡起的这 1 枚硬币
                res = smallest_sub_answer + 1
            
            # 在汇报给上层之前，先写进账本，方便以后直接查
            memo[amount] = res

            #所以最后每个节点return给上面的都是result，自己的最小subanswer+1
            return res
        
        # --- 最终调用与结果转换 ---
        final_result = dp(coins, amount)
        
        # 如果最终结果是 -100，按照 LeetCode 要求返回 -1，否则返回计算出的硬币数
        return final_result if final_result != -100 else -1




        