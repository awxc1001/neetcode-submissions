class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        #initalise the board
        board = [['.'] * n for _ in range(n)]
        rows = len(board)
        cols = len(board[0])

        #board 一开始和遍历的原本样子 = [
        #     ['.', 'Q', '.', '.'],  # 第 0 行：一个包含 4 个字符的列表
        #     ['.', '.', '.', 'Q'],  # 第 1 行：一个包含 4 个字符的列表
        #     ['Q', '.', '.', '.'],  # 第 2 行：一个包含 4 个字符的列表
        #     ['.', '.', 'Q', '.']   # 第 3 行：一个包含 4 个字符的列表
        # ]
        
        # 题目要求的输出是 List[str]（字符串列表），长这样：
        # [".Q..", "...Q", "Q...", "..Q."]
        # 对比一下就能发现：LeetCode 要求把每一行的字符列表（如 ['.', 'Q', '.', '.']），死死地粘合在一起，变成一个单独的字符串（如 ".Q.."）。

        #N 皇后不是没有 track，而是它的 queens 数组利用了“一行只能放一个”的完美棋盘特性，
        #把 track 隐式地融合进了一个固定长度的数组结构里，从而写起来更加简洁高效！
        #不需要显式 pop。因为直接通过 queens[row] = new_value 进行了覆盖（Overwrite）和重置撤销。
        result = []

        ## 注意：因为是一行行往下走，我们不再需要 start_c 参数了，只需要记录当前走到哪一行的 start_r
        def backtrack(start_r):
            #只要问题是“拆分型”或“组合型”（比如字符串切分、数字组合、排列、N皇后）：完全可以用你的这种“子问题返回值”的思路去写。
            #哪怕它不是 DP，代码也会写得非常漂亮、没有全局变量的污染。]

            #smallest problem is passed end of row, means no choice needed, a valid path reaced, meaning we got a valid board
            #convert the board to the correct format for the answer wanted
            if start_r == rows:
                #append correct answer
                format_ans = ["".join(r) for r in board]
                ## 赶紧趁着 函数里的答案 还没被销毁，把它“啪”地一下复制、存进外面长寿的大仓库里！
                result.append(format_ans)
                return

            #there are n columns of branches of decision you can make for this cur row
            cur_choices = len(board[start_r])
            #len要用range
            #each row of the board is a tracker, we just check if each grid is valid and backtrack downwards
            for col in range(cur_choices):
                if valid_q_grid(start_r, col):
                    #mark this board as queen and traverse downwards on this correct path
                    board[start_r][col] = 'Q'
                    backtrack(start_r + 1)
                    #cancel after a basecase callback
                    board[start_r][col] = "."
            


        def valid_q_grid(r , c):
            #既然我们是“从上往下”落子，这就意味着：当前行以下的所有格子，现在都还是干净的空地（全是 .），根本不可能有冲突！
            # 所以，当你准备在当前位置 (r, c) 落子时，你只需要抬头往上看，去检查已经放好皇后的那几行就行了。
            #记住不能over bound，而且要一直往上方向检查，同一行同一列，同一斜上都只能有一个Q

            #keep checking top
            row = r - 1
            col = c
            while row >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
            
            #keep checking previous top left and right
            row = r - 1
            col = c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1
            

            row = r - 1
            col = c + 1
            while row >= 0 and col <= rows - 1:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1

            #pass all check, return True
            return True
        

        start_row = 0
        backtrack(start_row)
        return result

                










        