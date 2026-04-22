class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #area = height diff * index diff
        #two pointer to form an area

        n = len(heights)
        left = 0
        right = n - 1
        max_area = -math.inf

        #2 <= height.length <= 1000
        while left < right:
            #height depnds the lower height
            valid_h = min(heights[left], heights[right])
            valid_w = right - left
            area = valid_h * valid_w
            if area > max_area:
                max_area = area
            
            #if we move pointer, we will reduce width naturally
            #so we move the one with lower height to bet a higher height
            if valid_h == heights[left]:
                left += 1
            elif valid_h == heights[right]:
                right -= 1
        
        return max_area

