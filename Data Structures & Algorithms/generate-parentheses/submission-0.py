class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        track = []
        answers = []

        def backtrack(left_count, right_count):
            #total left brackets == total right brackets == n
            #decision tree choice
            #left bracket can only be added when its left count < n
            #right brackets can only be added when its right count < left count, because any leading ) is invalid
            if left_count == right_count == n:
                #add a valid answer
                ans = "".join(track.copy())
                answers.append(ans)
                return


            if left_count < n:
                track.append("(")
                backtrack(left_count + 1, right_count)
                track.pop()
            
            if right_count < left_count:
                track.append(")")
                backtrack(left_count, right_count + 1)
                track.pop()

        #start count from 0 to backtrack
        backtrack(0, 0)

        return answers




            