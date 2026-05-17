from enum import Enum  # 👈 加上这一行，解决 Enum not defined 的问题！
class Status(Enum):
    CAN_BUY = 1
    HOLDING = 2
    SELL_FINISH = 3

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        #can only buy or sell on a single day, cannot do both on a single day
        #can only perform one buy and one sell within prices day array
        #choices branches are dynamic based on current node status

        #status are: 1. can buy 2. hold 3. sold finish
        #we start at day 0 of the array prices
        
        #top down smallest subproblem node as basecase,终点站
        #smallest problem
        #when already reach passed end of the array days, stop and return 0
        #when status already sold, stop and return 0 

        memo = {}
        def dp(i, status:Status):
            
            if (i, status) in memo:
                return memo[(i, status)]
            #smallest problem base case
            #when reached these condition, cannot contribute anything
            if i == n:
                return 0
            
            if status == Status.SELL_FINISH:
                return 0
            
            #max profit is recorded during sub answers collection
            #grow decison tree dynamically
            #initialise
            choices = []
            curr_best_ans = -math.inf

            #check current status to build the branch
            #we only care about current status and next day choices
            #choices.append( (明天是谁, 明天的身份, 今天的钱包变动)
            if status == Status.CAN_BUY:
                #update the status for future node
                buy_tuple = (i+1, Status.HOLDING, -prices[i])
                nothing_tuple = (i+1, Status.CAN_BUY, 0)
                # 👈 细节1：要把定义好的元组真正丢进 choices 篮子里！
                choices.append(buy_tuple)
                choices.append(nothing_tuple)
            
            elif status == Status.HOLDING:
                nothing_tuple = (i+1, Status.HOLDING, 0)
                #sell and gain current price
                sell_tuple = (i+1, Status.SELL_FINISH, prices[i])
                # 👈 细节1：要把定义好的元组真正丢进 choices 篮子里！
                choices.append(nothing_tuple)
                choices.append(sell_tuple)
            
            #dp check each future choice and get the best curr answer for curr
            for future_i, future_stat, cur_change in choices:
                sub_ans = dp(future_i, future_stat)
                curr_ans = cur_change + sub_ans
                # 👈 细节2：货比三家，新答案和历史最佳纪录pk
                curr_best_ans = max(curr_best_ans, curr_ans)
            
            memo[(i, status)] = curr_best_ans
            return curr_best_ans
            
        #begin dp from beginning
        start_day_i = 0
        initial_stat = Status.CAN_BUY
        max_profit = dp(start_day_i, initial_stat)
        return max_profit
        