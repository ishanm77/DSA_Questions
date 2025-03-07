
class Solution:
    def preToInfix(self, pre_exp):
        stack = []
        for char in reversed(pre_exp):
            if char.isalnum():  # If character is an operand (alphabet)
                stack.append(char)
            else:  # If character is an operator
                op1 = stack.pop()
                op2 = stack.pop()
                pre_exp = f"({op1}{char}{op2})"
                stack.append(pre_exp)
        return stack[-1]
