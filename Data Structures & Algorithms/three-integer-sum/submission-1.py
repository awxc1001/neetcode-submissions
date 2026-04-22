class Solution:
    def __init__(self):
        self.answers = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)

        for i in range(0, n):
            #only process the first number shown from left
            #any futher duplicate number on the right are skipped
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #find the required answer of each unique
            required = 0 - nums[i]
            #store each pair that adds to required
            required_list = self.two_sum(nums, i + 1, n - 1, required)
            #adds into answers for each pair
            for pair in required_list:
                self.answers.append([nums[i], pair[0], pair[1]])
            
        return self.answers

            
        
    def two_sum(self, nums, start, end, required):
        #two pointer to find sum target
        left = start
        right = end
        ans_list = []

        while left < right:
            sum = nums[left] + nums[right]
            if sum == required:
                ans_list.append([nums[left], nums[right]])
                #found one , move pointer to keep going
                left += 1
                #keep moving if its a duplicate
                while left < right and nums[left] == nums[left - 1]:
                        left += 1
            

            elif sum < required:
                left += 1
            
            elif sum > required:
                right -= 1
        
        return ans_list
