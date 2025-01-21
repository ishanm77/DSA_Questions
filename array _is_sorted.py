class Solution(object):
    def check(self, nums):
        count=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                count+=1
        return count<=1 and (count==0 or nums[-1]<=nums[0])