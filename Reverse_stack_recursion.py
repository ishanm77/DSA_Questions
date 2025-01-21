# Function to insert an element at the bottom of the stack
def insert_at_bottom(stack, item):
    if not stack:
        # If the stack is empty, push the item
        stack.append(item)
    else:
        # Pop the top element, recurse, and then push the top element back
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

# Function to reverse the stack
def reverse_stack(stack):
    if stack:
        # Pop the top element
        temp = stack.pop()
        # Reverse the remaining stack
        reverse_stack(stack)
        # Insert the popped element at the bottom of the reversed stack
        insert_at_bottom(stack, temp)