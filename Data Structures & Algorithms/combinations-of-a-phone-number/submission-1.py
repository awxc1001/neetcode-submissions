class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #make a num to letter str dict
        #题目给的是str，所以key最好str，简单一点，dict每个组合记得加逗号
        table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        #0 <= digits.length <= 4
        if len(digits) == 0:
            return []

        #do not make a big string, because then you dont know which letters belong to which number!
        # s = ""
        # for digit in digits:
        #     s.a
        
        track = []
        answers = []
        def backtrack(start_i):
            #base case reach when no more digit after each being decided
            if start_i == len(digits):
                #track现在是一个单一元素列表，answers会像 [['a', 'd'], ['a', 'e']]
                #所以要给track join变成string
                #因为 "".join() 会读取列表中的字符并创建一个全新的字符串。既然字符串本身就是不可变的，dont have to write copy
                answer = "".join(track.copy())
                #生成一个新的字符串需要遍历 track 列表，耗时 $O(N)$。总共有大约 $4^N$ 个叶子节点。最终结论：时间复杂度是 $O(N \cdot 4^N)$。
                #4 for worst case all 7 and 9 digits, 4^n leaf nodes
                answers.append(answer)
                return

            #decison tree, since string are mapped by digit order
            #we treat the start_i char to start the branch decision
            #eg 3 is "d" "e" "f" 3 branches, then next letter goes under these 3 branches and from another 3-4 branch for each
            #all branch fromed are valid in thise case


            #在回溯中，backtrack(start_i) 的 start_i 已经代表了当前的层数。
            #如果你写了 for i in range(start_i, len(digits))，程序会试图在第一层就把所有数字对应的字母都加一遍
            #在“分割字符串”题目里，你需要外层循环是因为你不知道这一刀该切多长，所以要用 for 循环试探 i 的位置。
            #但在“电话号码”题目里，每一层处理哪个数字是雷打不动的：
            # for i in (start_i, len(digits)):

           
            #choices
            digit = digits[start_i]
            letters = table[digit]
             #回溯里一个for循环做横向同一层选择，里面的backtrack，基于同一层各个选择做纵向下层选择。就这两个，多了就乱了
            for letter in letters:
                #current choice added. this is same level letter
                track.append(letter)
                #go add next digit choice for next decsion branch
                #keep going for next level
                backtrack(start_i + 1)
                #go back
                track.pop()

                 
        backtrack(0)
        return answers

# --- 面试时的测试代码写在下面 ---
if __name__ == "__main__":
    sol = Solution()

    # Case 1: 常规输入
    res1 = sol.letterCombinations("23")
    print(f"Test '23': {res1}") 
    # 预期: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    # Case 2: 空输入
    res2 = sol.letterCombinations("")
    print(f"Test '': {res2}")
    # 预期: []

    # Case 3: 包含 4 个字母的情况
    res3 = sol.letterCombinations("7")
    print(f"Test '7': {res3}")
    # 预期: ['p', 'q', 'r', 's']

    # 自动化断言测试 (更加专业)
    assert len(sol.letterCombinations("23")) == 9
    assert "ad" in sol.letterCombinations("23")
    print("\n✅ All test cases passed!")
