class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_let_count = {}
        for ch in t:
            t_let_count[ch] = t_let_count.get(ch, 0) + 1

        window = {}
        window_valid = 0

        fast = 0
        slow = 0
        s_len = len(s)
        t_len = len(t)

        min_start_i = math.inf
        min_sub_len = math.inf

        while fast < s_len:
            ch = s[fast]
            window[ch] = window.get(ch, 0) + 1
            fast += 1

            #check if this ch is in t and see if its count reaches valid
            if ch in t_let_count:
                if window[ch] == t_let_count[ch]:
                    window_valid += 1
            

            #try shrink when window can cover all t_let_count
            while slow < fast and window_valid == len(t_let_count):
                #record a valid answer first 
                window_size = fast - slow
                if window_size < min_sub_len:
                    min_start_i = slow
                    min_sub_len = window_size

                #after record perform del
                ch_del = s[slow]
                ## 关键逻辑：如果要踢掉的是重要角色
                # 且踢掉前它刚好满足数量，那踢掉后有效计数就要减 1
                #窗口里的字符可能“溢出”了。
                #我们需要区分**“刚刚好满足”和“绰绰有余”**这两种状态。
                if ch_del in t_let_count:
                    if window[ch_del] == t_let_count[ch_del]:
                        window_valid -= 1

                #perform removal on window
                window[ch_del] = window.get(ch_del) - 1
                if window[ch_del] == 0:
                    del window[ch_del]
                
                #increase slow pointer
                slow += 1
        
        if min_start_i == math.inf:
            return ""
        return s[min_start_i: min_start_i + min_sub_len]
    

            
