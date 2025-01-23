def binarysearch(nums,n):
    start=0
    end=len(nums)-1
    while start<=end:
        mid=start+(end-start)//2
        midvalue=nums[mid]
        if midvalue==n:
            return mid
        elif n<midvalue:
            end=mid-1
        else:
            start=mid+1
    return None

nums_a=[1,2,3,4,4,5,6,7,8,9]
n_a=9

print(binarysearch(nums_a,n_a))