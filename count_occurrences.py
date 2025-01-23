class Solution(object):
    def searchRange(self,n, arr, x):
        def findleftindex(arr,x):
            left=0
            right=n-1
            while left<=right:
                mid=left+(right-left)//2
                if arr[mid]<x:
                    left=mid+1
                else:
                    right= mid-1
            return left
        def findrightindex(arr,x):
            left=0
            right=n-1
            while left<=right:
                mid=left+(right-left)//2
                if arr[mid]<=x:
                    left=mid+1
                else:
                    right= mid-1
            return right
        first_index=findleftindex(arr,x)
        last_index=findrightindex(arr,x)
        if first_index<=last_index:
            return last_index-first_index+1
        else:
            return 0