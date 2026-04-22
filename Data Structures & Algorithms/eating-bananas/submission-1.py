class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #given h and piles, find k eat per h
        #1 <= piles[i] <= 1,000,000,000
        #left and right are eating speed per hour
        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            mid_hour = self.speed_to_hour(piles, mid)
            #find the minumum speed, so left bound
            if mid_hour == h:
                right = mid - 1
            if mid_hour < h:
                right = mid - 1
            if mid_hour > h:
                left = mid + 1
        #in a valid range, no need do off boundry check
        return left
            
    def speed_to_hour(self, piles: List[int], speed: int):
        #begin eating with a given speed per hour
        total_hour = 0
        for pile in piles:
            cur_pile_hour = pile // speed
            if pile % speed > 0:
                cur_pile_hour += 1
            # add to total_hour and restart another pile
            total_hour += cur_pile_hour
            cur_pile_hour = 0

        return total_hour

        