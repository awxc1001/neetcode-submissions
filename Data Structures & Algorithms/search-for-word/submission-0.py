class Solution:
    def __init__(self):
        self.visited = set()
        self.answer = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        #try every grid in matrix to find one that can link neighbor grids to form a word
        rows = len(board)
        cols = len(board[0])

        ch_i = 0

        for row in range(rows):
            for col in range(cols):
                # 只要有一个起点成功，就直接返回 True
                if self.dfs(row, col, board, rows, cols, word, 0):
                    self.answer = True
        
        return self.answer


    def dfs(self, cur_r, cur_c, board, rows, cols, word, ch_i):
        #common base case
        if cur_r < 0 or cur_c < 0 or cur_r == rows or cur_c == cols:
            return False
        
        if (cur_r, cur_c) in self.visited:
            return False
        
        if board[cur_r][cur_c] != word[ch_i]:
            return False

        # if ch_i == len(word):
        #     return True

        # 3. 成功出口：当前字符匹配且是最后一个字符
        if ch_i == len(word) - 1:
            return True
        

        self.visited.add((cur_r, cur_c))

        founded = self.dfs(cur_r + 1, cur_c, board,  rows, cols, word, ch_i + 1) or self.dfs(cur_r - 1, cur_c, board, rows, cols, word, ch_i + 1) or self.dfs(cur_r, cur_c + 1, board, rows, cols, word, ch_i + 1) or self.dfs(cur_r, cur_c - 1, board, rows, cols, word, ch_i + 1)
        
        self.visited.remove((cur_r, cur_c))

        return founded


        




