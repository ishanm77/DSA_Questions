class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, s):
        precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
        output = []
        stack = []

        for char in s:
            if char.isalnum():  # Operand
                output.append(char)
            elif char in precedence:  # Operator
                while stack and precedence.get(stack[-1], 0) >= precedence[char]:
                    output.append(stack.pop())
                stack.append(char)
            elif char == '(':  # Left parenthesis
                stack.append(char)
            elif char == ')':  # Right parenthesis
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Remove '('

        while stack:  # Pop remaining operators
            output.append(stack.pop())

        return "".join(output)