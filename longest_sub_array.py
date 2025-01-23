class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        length=0
        for i in range(n):
            current=0
            for j in range(i,n):
                current += arr[j]
                if current==k:
                    length=max(length,j - i + 1)
        return length
               