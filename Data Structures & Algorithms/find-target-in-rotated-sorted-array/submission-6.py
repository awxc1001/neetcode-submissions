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
            
           # --- 场景一：左半边 [left...mid] 是整齐递增的 ---
            if nums[left] <= nums[mid]:
                
                # 情况 A：target 确实在左边这个整齐的范围内
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                
                # 情况 B：target 比左边最小的还小 (说明它可能在右边那个“掉下去”的区间)
                elif target < nums[left]:
                    left = mid + 1
                
                # 情况 C：target 比左边最大的(mid)还大 (说明它在更右边)
                elif target > nums[mid]:
                    left = mid + 1

            # --- 场景二：右半边 [mid...right] 是整齐递增的 ---
            # (如果场景一不成立，场景二一定成立)
            elif nums[mid] <= nums[right]:
                
                # 情况 D：target 确实在右边这个整齐的范围内
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                
                # 情况 E：target 比右边最大的还大 (说明它可能在左边那个“高起”的区间)
                elif target > nums[right]:
                    right = mid - 1
                
                # 情况 F：target 比右边最小的(mid)还小 (说明它在更左边)
                elif target < nums[mid]:
                    right = mid - 1
            
        return -1


            


       
    