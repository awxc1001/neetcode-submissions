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

             #map always save the older ones, smaller index
            if need in num_index_map:
                return [num_index_map[need], index]

            #先问后存，不然 6 - 3 = 3，3被存入，然后need检测return[0,0]
            if need not in num_index_map:
                #record and keep going
                num_index_map[num] = index     
        return
            


            


        
        