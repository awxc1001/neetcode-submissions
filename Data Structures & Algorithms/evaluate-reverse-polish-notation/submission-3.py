class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        #assume every input is valid
        #final_ans 的误用：RPN 的最终结果就是计算结束时栈中剩下的最后一个数字。你定义的 final_ans += ans 会累加中间过程的每一部结果，这在逻辑上是不正确的。
        #在复杂的表达式中，中间结果可能被减掉、除掉或者作为乘数，而不是被加上去。
        #
        for token in tokens:

            if token == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                ans = int(num1) + int(num2)
                stack.append(str(ans))
            
            elif token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                ans = int(num2) - int(num1)
                stack.append(str(ans))
            
            elif token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                 #在 Python 中，// 是向下取整（Floor Division）。例如：6 // -132 在 Python 中结果是 -1（因为 $-0.045$ 向下取整是 $-1$）。
                #但题目要求是向零取整（Truncate toward zero），即结果应该是 0。解决办法：使用 int(num2 / num1)。Python 的浮点数除法后转 int 会自动舍弃小数部分，实现向零取整。
                # ans = int(num2) // int(num1)
                ans = int (int(num2) / int(num1))
                stack.append(str(ans))
            
            elif token == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                ans = int(num2) * int(num1)
                stack.append(str(ans)) 
            
            #not notation, just append num
            else:
                stack.append(token)
        
        return int(stack[-1])
        

            
        