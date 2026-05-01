class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #9 x 9 board
        rows = len(board)
        cols = len(board[0])

        #scan every cell in row based
        for r in range(rows):
            #每一新行都reset，就看单一行是不是都unique
            row_set = set()
            for c in range(cols):
                #skip no num cell
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_set:
                    return False
                row_set.add(board[r][c])
        
        #scan every cell in col based
        for c in range(cols):
            #每一个新column都reset，就看单一列是不是都unique
            col_set = set()
            for r in range(rows):
                #skip no num cell
                if board[r][c] == ".":
                    continue
                if board[r][c] in col_set:
                    return False
                col_set.add(board[r][c])
        
        #now scan square by square for 9 times
        #note sqaure num is from 0 - 8
        for square_num in range(9):
            square_set = set()
            #9x9 with three 3x3 sqaure as a group
            #find the square row and col group
            #group  start from 0,
            #for square 0 to 2, 2 // 3 = 0
            #2 % 3 =2
            #for last square num 8, 8 // 3 =2, 8 % 3 = 2
            square_group_row = square_num // 3
            square_group_col = square_num % 3
            #find this square start row and col in in the board
            start_r = square_group_row * 3
            start_c = square_group_col * 3
            #now we check this 3x3 sqaure inside
            for r in range(start_r, start_r + 3):
                for c in range(start_c, start_c + 3):
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in square_set:
                        return False
                    square_set.add(board[r][c])
        
        #after all check, return True
        return True


             
            



            



        