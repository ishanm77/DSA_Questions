def sort_stack(stack):
    # Auxiliary stack
    temp_stack = []
    
    while stack:
        # Pop the top element from the original stack
        current = stack.pop()
        
        # Move elements from temp_stack back to stack if they are smaller than the current element
        while temp_stack and temp_stack[-1] < current:
            stack.append(temp_stack.pop())
        
        # Push the current element onto the temp_stack
        temp_stack.append(current)
    
    # Move elements back to the original stack
    while temp_stack:
        stack.append(temp_stack.pop())
    
    return stack