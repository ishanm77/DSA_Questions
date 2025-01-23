class Solution(object):
    def searchRange(self, nums, target):
        def findleftindex(nums,target):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]<target:
                    left=mid+1
                else:
                    right= mid-1
            return left
        def findrightindex(nums,target):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]<=target:
                    left=mid+1
                else:
                    right= mid-1
            return right
        first_index=findleftindex(nums,target)
        last_index=findrightindex(nums,target)
        if first_index<=last_index:
            return [first_index,last_index]
        else:
            return [-1,-1]