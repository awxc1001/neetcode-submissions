class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        #rotated means one or two linear range in this array
        while left <= right:
            #find a range where left <= mid <= right 
            #then left must be smallest
            #initally we dont know whch linear range is mid in
            #or if the array is rotated nack to same array
            mid = left + (right - left) // 2
            
            if (nums[left] <= nums[mid] <= nums[right]):
                return nums[left]
            
            # 2. 如果 mid 的值比 left 还要小
            # 说明：从 left 到 mid 之间一定发生了“跳水”（断层在左边）
            # 例子: [4, 5, 1, 2, 3], left=4, mid=1
            elif nums[mid] < nums[left]:
                right = mid 
            
            # 3. 如果 mid 的值比 right 还要大
            # 说明：从 mid 到 right 之间发生了“跳水”（断层在右边）
            # 例子: [3, 4, 5, 6, 1], mid=6, right=1
            elif nums[mid] > nums[right]:
                # 最小值一定在 mid 的右边
                left = mid + 1
            
        return - 1
        