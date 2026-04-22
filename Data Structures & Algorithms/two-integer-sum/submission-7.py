class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 想象你在走一条单行道，你手里有一个记事本（哈希表）。
        # 每走一步：先看一眼记事本。
        # 问一个问题：我想要的东西（补数）在记事本上吗？
        # 如果在：结束，成功。
        # 如果不在：把我现在的数字和位置写在记事本上，继续往前走，绝不回头。

        #看答案要返回什么，要返回的是index，所以我们num做key查找
        #map with num as key, index as value
        num_index_map = {}

        for index, num in enumerate(nums):
            #instaead of a + b = target, we have target - a, so lets find b
            need = target - num
            
            #先问后存
            if need not in num_index_map:
                #record and keep going
                num_index_map[num] = index  

            if need in num_index_map:
                # exactly one pair of indices i and j, cannot have same index. 
                #avoid dup conditon like incase [5,5] = 10, return [0,0] instead of return [0, 1]
                if num_index_map[need] != index:
                    return [num_index_map[need], index]

               
        return
            


            


        
        