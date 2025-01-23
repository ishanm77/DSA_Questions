def findFloor(self,A,N,X):
        low=0
        high=N-1
        while low<=high:
            mid=low+(high-low)//2
            if A[mid]==X:
                return mid
            elif A[mid]<X:
                low=mid+1
            else:
                high=mid-1
        return high
        