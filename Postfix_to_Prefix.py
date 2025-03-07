class Solution:
    def postToPre(self, post_exp):
        stack = []
        for char in post_exp:
            if char.isalnum():  # If character is an operand (alphabet)
                stack.append(char)
            else:  # If character is an operator
                op2 = stack.pop()
                op1 = stack.pop()
                post_exp = f"{char}{op1}{op2}"
                stack.append(post_exp)
        return stack[-1]