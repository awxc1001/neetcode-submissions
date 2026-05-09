class Solution:
    def isValid(self, s: str) -> bool:
        #close right as key, open left as value, dont write it wrong
        close_open = {")":"(", "]":"[", "}":"{"}
        stk = []
        #we can append as many open left into stack, but when there is right close there must be a most recent matching left that just appended
        #pop the top of the stack (most recent) to compare
        #repeat until all left are processed in steack esle false
        for ch in s:
            if ch in close_open:
                #check if stack has anything
                if stk:
                    match_open = close_open[ch]
                    if match_open != stk.pop():
                        return False
                else:
                    #empty stack cannot match a right
                    return False
            #since only open left and closing right in str, just append the left if not closing parent
            #append unporcessed left open only
            else:
                stk.append(ch)
        
        #stk not empty means some left are unprocessed, incorrect
        return False if stk else True


def test():
    sol = Solution()
    cases = [
        ("()", True),
        ("(]", False),
        ("([)]", False)
    ]
    
    for s, expected in cases:
        res = sol.isValid(s)
        # 用这种方式代替 assert，既有反馈又专业
        if res == expected:
            print(f" Pass: Input '{s}', Output {res}")
        else:
            print(f" Fail: Input '{s}', Expected {expected}, but got {res}")

test()
