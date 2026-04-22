class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        fast = 0   #右边界快指针
        slow_i = 0          # 窗口左边界（慢指针）
        window = {}         # 账本：记录当前窗口内每个字符出现的频率 {字符: 数量}
        window_max_freq = 0 # 巅峰战力：记录到目前为止，窗口内出现频率最高的字符次数（历史最高纪录）
        res = 0             # 最终答案：记录满足条件的最长窗口长度

        # 使用 fast 作为窗口右边界（快指针），自动逐位右移探索字符串
        for fast in range(n):
            # 1. 进窗：取出当前字符，并在账本里把它的出现次数 +1
            ch = s[fast]
            window[ch] = window.get(ch, 0) + 1
            
            # 2. 刷新纪录：如果新进窗的这个字符让频率变高了，更新我们的“巅峰战力”记录
            # 这是为了知道窗口里那个不需要被修改的“主角”最多能有多少个
            window_max_freq = max(window_max_freq, window[ch])

            # 3. 门禁检查（核心公式）：
            # 当前窗口长度 = fast - slow_i + 1
            # 配角数量（需要被改掉的字符） = 当前窗口长度 - 巅峰战力
            # 如果配角数量 > k，说明你手里的“万能变身卡”不够用了，保安（while）要拦住你
            while (fast - slow_i + 1) - window_max_freq > k:
                # 缩窗：把窗口最左边的字符踢出去
                ch_del = s[slow_i]
                window[ch_del] -= 1
                # 慢指针右移，直到窗口重新变得“合法”（变身卡能覆盖所有配角）
                slow_i += 1
            
            # 4. 结算：此时保安放行（while 循环结束），说明当前窗口在 k 的支持下是合法的
            # 记录下我们在探索过程中见过的最长合法窗口
            valid_window_size = fast - slow_i + 1
            res = max(res, valid_window_size)

        # 最终返回这个“巅峰长度”
        return res