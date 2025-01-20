from typing import List
class Solution:
    def largest(self, arr : List[int]) -> int:
        largest=arr[0]
        for num in arr:
            if num>largest:
                largest=num
        return largest