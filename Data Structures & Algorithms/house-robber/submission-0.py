class Solution:
    def rob(self, nums: List[int]) -> int:
        #treat each choice as a index choice, each choice contributes
        #its max amount money and gives back to parent big problem
        #cannot rob two adj house, so rob choice from start is
        choices = [0, 1]

        #你可以把大问题定义成：
        #dp(i) 表示：从第 i 间房子开始往后偷，最多能偷多少钱
        
        #we use index as view point not distance or amount like other dp
        memo = {}
        def dp(i, choices):
            #stop when goes over nums
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            #initilaise current best answer of each node
            best_sub_ans = 0
            #check current house index money
            current_h_money = nums[i]
            #now go over each choices
            for choice in choices:
                #if rob this one, can only rob next next
                if choice == 0:
                    sub_ans_1 = current_h_money + dp(i + 2, choices)
                elif choice == 1:
                    sub_ans_2 = dp(i + 1, choices)
            
            #get the best answer
            best_sub_ans = max(sub_ans_1, sub_ans_2)
            memo[i] = best_sub_ans

            return best_sub_ans


    
    #beacause we given nums, we start from 0 to get all possible answers
    #and get the best one
        return dp(0, choices) 
        