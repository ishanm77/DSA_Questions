class Solution(object):
    def rotate(self, nums, k):
       n=len(nums)
       k%=n
    #    nums[:]=concatenation
    # nums[-k:]= takes all the last k elements
    # nums[:-k]=-takes all the elements except the last k elements
       nums[:]=nums[-k:]+ nums[:-k]