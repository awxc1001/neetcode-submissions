class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left <= right:
            #we only compare alnum char in this question, special char are ignored
            if s[left].isalnum() is False:
                left +=1
            #we only compare alnum char in this question, special char are ignored
            elif s[right].isalnum() is False:
                right -= 1
            
            #now compare and return if False
            elif s[left].lower() != s[right].lower():
                return False
            
            #after skiping and compare pass, we can then reduce pointer range
            else:
                left += 1
                right -= 1
            
        return True