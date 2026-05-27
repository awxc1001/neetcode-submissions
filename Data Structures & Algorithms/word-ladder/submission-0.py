class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 将 wordList 转换为 HashSet，加速查找
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # 直接套用 BFS 算法框架
        q = collections.deque([beginWord])
        visited = set([beginWord])
        step = 1
        while q:
            sz = len(q)
            for i in range(sz):
                # 穷举 curWord 修改一个字符能得到的单词
                # 即对每个字符，穷举 26 个字母
                curWord = q.popleft()
                chars = list(curWord)
                # 开始穷举每一位字符 curWord[j]
                for j in range(len(curWord)):
                    originChar = chars[j]
                    # 对每一位穷举 26 个字母
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == originChar:
                            continue
                        chars[j] = c
                        # 如果构成的新单词在 wordSet 中，就是找到了一个可行的下一步
                        newWord = ''.join(chars)
                        if newWord in wordSet and newWord not in visited:
                            if newWord == endWord:
                                return step + 1
                            q.append(newWord)
                            visited.add(newWord)
                    # 最后别忘了把 curWord[j] 恢复
                    chars[j] = originChar
            # 这里增加步数
            step += 1
        return 0