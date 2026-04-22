class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        s1_letter_count = [0] * 26

        for ch in s1:
            letter_i = ord(ch) - ord("a")
            s1_letter_count[letter_i] += 1
        
        window = [0] * 26

        #sliding window
        fast = 0
        slow = 0

        for fast in range(s2_len):
            ch = s2[fast]
            letter_i = ord(ch) - ord("a")
            window[letter_i] += 1

            #shrink conddition if elements in window(window_size)
            #is over s1_len
            while slow < fast and (fast - slow + 1) > s1_len:
                ch_del = s2[slow]
                letter_i = ord(ch_del) - ord("a")
                window[letter_i] -= 1
                slow += 1
            
            #now every shrink this is a valid window with size <= len(s1)
            #check if we got a solution
            if s1_letter_count == window:
                return True
            
        return False

