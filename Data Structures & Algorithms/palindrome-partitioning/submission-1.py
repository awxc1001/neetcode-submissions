class Solution:
    def partition(self, s: str) -> List[List[str]]:
        track = []
        answers = []
        s_len = len(s)


        def backtrack(start, s_len):
            #base casereach if there is no more you can slice
            #no more ch in the str
            if start == s_len:
                answers.append(track.copy())
                return


            #decision logic, choice is made base on if this branch can pass the palindrome test
            #if fail palidrome, rest is cut off
            #we do it for every node's decision
            for i in range(start, s_len):
                #这样写只会取一个ch
                # s_choice = s[i:i+1]
                #这样写可以取多个
                s_choice = s[start : i + 1]
                if self.is_palin(s_choice):
                    track.append(s_choice)
                    backtrack(i+1, s_len)
                    #pop没有input，弹出新插入的
                    #return case reach， restore level by level
                    track.pop()
                else:
                    continue

        backtrack(0, s_len)

        return answers



    def is_palin(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True






        