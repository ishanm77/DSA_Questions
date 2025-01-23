class Solution(object):
    def maxDepth(self, s):
        result=0
        current=0
        for i in s:
            if i=="(":
                current += 1
            elif i== ")":
                current -= 1
            result=max(result,current)
        return result