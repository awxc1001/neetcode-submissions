class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #peform binary search on row first
        rows, cols = len(matrix), len(matrix[0])

        #binary on rows
        top = 0
        bot = rows - 1
        target_row = 0
        while top <= bot:
            mid = (top + bot) // 2
            #check largest in a row
            #每一行的范围是 [row_start, row_end]
            if matrix[mid][-1] < target:
                #go down
                top = mid + 1

            #check smallest in a row
            elif matrix[mid][0] > target:
                #go up
                bot = mid - 1
            else:
                #find the inclusive range
                #*matrix[row][0] <= target <= matrix[row][-1]
                target_row = mid
                break

        #binary tree on target row
        left = 0 
        right = cols - 1
        while left <= right:
            mid = (left + right) // 2

            if matrix[target_row][mid] == target:
                return True
            
            elif matrix[target_row][mid] < target:
                left = mid + 1
            
            elif matrix[target_row][mid] > target:
                right = mid - 1
        
        return False
            
        
        