class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use hashset to quick locate a num and situation around
        #since there are duplicae in nums, lets remove them using set
        #0 <= nums.length <= 1000
        if not nums:
            return 0

        num_set = set()
        #add in hashset O(1), * numsize
        for num in nums:
            num_set.add(num)
        
        #now locate the start of each num
        #since consec sequence want us to have exactly 1 greater
        #a start means this num has no exactly 1 smaller num
        #in means lookup/search, O(1) time in hash, just hash and find
        max_res = -math.inf
        for num in num_set:
            if num - 1 in num_set:
                #not a start of sequen, skip
                continue
            #now at start of squence
            curr_len = 1
            #check how much sequence it has
            while num + 1 in num_set:
                curr_len +=1
                #update num as well
                num = num + 1
            #end of a sequence check, update the max
            max_res = max(max_res, curr_len)
        
        return max_res
            
        