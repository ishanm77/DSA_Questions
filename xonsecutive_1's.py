class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max1=0
        count=0
        for num in nums:
            if num==1:
                count+=1
            else:
                max1=max(max1,count)
                count=0
            max1=max(max1,count)
        return max1
        