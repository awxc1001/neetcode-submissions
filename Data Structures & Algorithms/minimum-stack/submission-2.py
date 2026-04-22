class MinStack:

    def __init__(self):
        #当前最小
        self.mini = math.inf
        self.stack = []

        #special stack
        #min_stack 记录的是当前最小值的变更历史，
        #并且和主栈同步，如果pop的是当前最小
        #mini_stack也一起pop
        self.mini_stack = []

    def push(self, val: int) -> None:
        #empty stack dont matter
        #if stack not empty check smallest
        if self.stack:
            #你想想这时应该发生什么：
            # 第一个 2 入栈，最小值是 2
            # 第二个 2 入栈，最小值还是 2
            # 弹出一个 2 后，最小值 仍然应该是 2
            # 但如果你第二个 2 没有进 mini_stack，
            # 那弹掉一个 2 时，历史就少记了一次。
            if val <= self.mini:
                self.mini = val
                #guarantee each mini stack top
                #always the current smallest
                self.mini_stack.append(val)
            
        else:
            self.mini = val
            self.mini_stack.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        removed = self.stack.pop()
        if removed == self.mini:
            self.mini_stack.pop()
            if self.mini_stack:
                self.mini = self.mini_stack[-1]
            else:
                #empty self.mini_stack, reset
                self.mini = math.inf

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mini
