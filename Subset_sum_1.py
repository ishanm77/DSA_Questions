def subset_sums(arr):
    def helper(index, current_sum):
        if index == len(arr):
            result.append(current_sum)
            return
        # Include the current element
        helper(index + 1, current_sum + arr[index])
        # Exclude the current element
        helper(index + 1, current_sum)

    result = []
    helper(0, 0)
    return result

# Example usage:
arr = [1, 2, 3]
print(subset_sums(arr))  # Output: [6, 5, 4, 3, 3, 2, 1, 0] (order may vary)

