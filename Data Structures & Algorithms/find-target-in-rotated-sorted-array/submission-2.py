class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        #since roated we know there are two ranges
        #left sorted range, right sorted range
        #lets find out where mid sits and perform binary search
        # all elements are unique
        while left <= right:
            mid = left + (right - left) // 2

            #we already check mid, so can move right left + 1 -1
            #不像 find smallest
            if nums[mid] == target:
                return mid
            
            #if [left, mid] is sorted
            if nums[left] <= nums[mid]:
                #now we see if target lies in a ascending range order
                if  nums[left] <= target < nums[mid]:
                    right = mid - 1
                # 情况 B：target 比左边最小的还小 (说明它可能在右边那个“掉下去”的区间)
                elif target < nums[left]:
                    left = mid + 1
                
                # 情况 C：target 比左边最大的(mid)还大 (说明它在更右边)
                elif target > nums[mid]:
                    left = mid + 1
            
            #if [mid, right] is sorted
            elif nums[mid] <= nums[right]:
                #now we see if target lies in a ascending range order
                if  nums[mid] < target <= nums[right]:
                    left = mid + 1
                elif target > nums[right]:                 
                    right = mid - 1
                elif target < nums[mid]:       
                    right = mid - 1
            
        return -1


            


       
    