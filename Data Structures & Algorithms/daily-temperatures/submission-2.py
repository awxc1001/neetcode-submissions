class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        #monostack that only stores biggest bottom, and smallest on stack top
        #any unmatching onese will be poped to main the order
        min_stack = []
        #we store the index of min_stack for index diff calculating

        for i in range(n):
            curr_temp = temperatures[i]
            #maintain the mono min stack rule
            #if empty stack, just add the index in
            if not min_stack:
                min_stack.append(i)
            
            #keep pop out the ones in min_stack from top that is smaller than curr_temp to maintain biggest bot to smallest top order
            while min_stack and curr_temp > temperatures[ min_stack[-1] ]:
                #keep poping till nothing left or until curr_temp can be append to maintain the min_stack order
                past_i = min_stack.pop()
                result[past_i] = i - past_i
            
            #不管是都pop掉了，还是没有，都要append这个最新的
            min_stack.append(i)
        
        return result


def test():
    sol = Solution()
    #list of case and ans tuples
    cases = [
        ([12, 13, 14, 11], [1, 1, 0 , 0]),
        ([22, 21, 20], [0, 0 , 0]),
        ([2], [0]),
        ([12, 15, 11, 40, 32], [1, 2, 1, 0, 0])
    ]
    for case, exp in cases:
        print(case, "->", sol.dailyTemperatures(case), "expected:", exp)

test()   



            



            

            
            
        