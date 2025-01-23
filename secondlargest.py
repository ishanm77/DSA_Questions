class Solution:
    def getSecondLargest(self, arr):
        # Descending order conversion
        arr.sort(reverse=True)
        for i in range(1,len(arr)):
            if arr[i]!=arr[0]:
                return arr[i]

        return -1