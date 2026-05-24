class TimeMap:

    def __init__(self):
        self.store = {}
    
    def set(self, key: str, val: str, timestamp: int) -> None:
        #the key is for hash key
        #val pair is list of tuple values(val, timestap)
        tuple_info = (val, timestamp)
        val_time_list = self.store.get(key, [])
        val_time_list.append(tuple_info)
        #because intinally if you get there is nothign and default val, it wont assoicate with orignal dict
        #has to reassign backto dict
        self.store[key] = val_time_list

    def get(self, key: str, timestamp: int) -> str:
        #All the timestamps of set are strictly increasing.
        # linear time, Returns a value such that set was called previously, with timestamp_prev <= timestamp
        #binary search closest smallerthan timestamp given
        answer = ""
        val_time_list = self.store.get(key, [])
        #If there are no values, it returns "".
        if not val_time_list:
            return ""
        
        #len in python source code is acutally a bult-in size counter to return list size, still O(1)
        left =0
        right = len(val_time_list) - 1

        #close boundry check
        while left <= right:
            mid = (left + right) // 2
            #list stores (val, timestamp)
            mid_time = val_time_list[mid][1]

            #if time match exact, just return the val
            if mid_time == timestamp:
                answer = val_time_list[mid][0]
                return answer
            
            #closing the right bound
            # 1 3 5 6 7   target = 3
            if mid_time > timestamp:
                right = mid - 1

            #closing left boundry
            if mid_time < timestamp:
                  #在 while left <= right 的闭区间二分查找结束时，如果没找到精确匹配的值，right 和 left 指针最终一定会一起指向小于且最接近 timestamp 的那个索引
                answer = val_time_list[mid][0]
                left = mid + 1
        
        return answer





        




        
