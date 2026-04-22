class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_map = collections.defaultdict(list)

        for str in strs:
            #字符串不可变 (Strings are Immutable)
            # 在 Python 中，字符串是不能被修改的。你不能对一个字符串说：“请把你内部的字母排个序”。
            # "eat".sort() 会报错，因为字符串没有这个方法。
            # sorted("eat") 则是把字符串里的字符一个个拿出来，排好序放进一个新列表。
            sorted_str = "".join(sorted(str))

            #add word in to list, sorted_str is the key
            sorted_str_map[sorted_str].append(str)
        
        #return list of word list
        result = []
        for key in sorted_str_map:
            result.append(sorted_str_map[key])
        
        return result
        



        