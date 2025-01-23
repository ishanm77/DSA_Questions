class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        left,right=0,N-1
        while left<=right:
            mid=left+(right-left)//2
            if arr[mid]==K:
                return 1
            elif arr[mid]<K:
                left=mid+1
            else:
                right=mid-1
        return -1