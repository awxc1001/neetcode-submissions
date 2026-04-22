class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since 1-index based, can increase the answer by 1 off when return
        #always one valid solution with index1 < index 2
        
        n = len(numbers)
        left = 0
        right = n - 1

        # sorted in non-decreasing order.
        while left < right:
            l_num = numbers[left]
            r_num = numbers[right]
            sum = l_num + r_num

            if sum == target:
                return [left + 1, right + 1]

            elif sum > target:
                right -= 1
            
            elif sum < target:
                left += 1
        