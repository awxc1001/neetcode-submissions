class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table_s = {}
        table_t = {}

        for ch in s:
            table_s[ch] = table_s.get(ch, 0) + 1
        
        for ch in t:
            table_t[ch] = table_t.get(ch, 0) + 1
        
        #in python, two dictionral are equal if key value pair all same
        #other language wont do
        return table_s == table_t
        

        
