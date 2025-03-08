
class Solution:
    def postToInfix(self, postfix):
        stack = []
        for char in postfix:
            if char.isalnum():  # If character is an operand (alphabet)
                stack.append(char)
            else:  # If character is an operator
                op2 = stack.pop()
                op1 = stack.pop()
                new_expr = f"({op1}{char}{op2})"
                stack.append(new_expr)
        return stack[-1]