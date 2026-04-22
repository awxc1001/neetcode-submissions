class Solution:

    def encode(self, strs: List[str]) -> str:
        #we encode charcount and # and front of each str
        encoded_str = ""

        for s in strs:
            char_count = len(s)
            tag = str(char_count) + "#"
            encoded_str += tag + s
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        #start from begin of encoded string
        res = []
        start_i = 0

        #can have 15 #, 200#, 10000#, need to move j
        while start_i < len(s):
            j = start_i
            #start from some and move j to find #
            while s[j] != "#":
                j += 1

            #now j reached # find the length
            str_len = int(s[start_i:j])
            #now at start char of each str
            start_i = j + 1

            #set up right boundry for slicing
            right_boundry = start_i + str_len
            res.append(s[start_i:right_boundry])
            start_i = right_boundry
        
        return res




            
