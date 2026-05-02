class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        pre_product = [0] * (n + 1)
        suff_product = [0] * (n + 1)
        
        pre_product[0] = suff_product[-1] = 1

        #fill up the pre and suff
        for i in range(n):
            pre_product[i + 1] = pre_product[i] * nums[i]
        
        for i in range(n-1, -1, -1):
            #index n, last index, end of suffix is 1, here we start from n-1 index, end of nums
            suff_product[i] = suff_product[i + 1] * nums[i]
        

        # 当我们计算第 i 个位置（nums[i]）时：

        # 左边：就是 [0, i) 这个区间，对应的正是 pre_product[i]。

        # 右边：就是 [i + 1, n) 这个区间，对应的正是 suff_product[i + 1]。
        pro_array = [0 for i in range(n)]
        for i in range(n):
            pro_array[i] = pre_product[i] * suff_product[i + 1]
        
        return pro_array
        

        #2. 为什么是 i 和 i+1？
        # 这是最绕的地方。我们用最土的办法，数个数：

        # 假设我们要算 Index 2（即数字 c）的结果：

        # 它左边有几个数？两个（nums[0], nums[1] c:nums[2], nums[3]）。

        # 在你的 pre_product 数组里：

        # pre_product[0] 是 0 个数的乘积（等于 1）

        # pre_product[1] 是 1 个数的乘积（nums[0]）

        # pre_product[2] 是 2 个数的乘积（nums[0]*nums[1]）—— 正好是你需要的！

        # 它右边有几个数？一个（nums[3]）。

        # 在你的 suff_product 数组里（倒着数）：

        # suff_product[4] 是 0 个数的乘积（等于 1）

        # suff_product[3] 是 1 个数的乘积（nums[3]） —— 正好也是你需要的！

        # 所以：res[2] = pre_product[2] * suff_product[3]。
        # 通用公式就是：res[i] = pre_product[i] * suff_product[i+1]。


        