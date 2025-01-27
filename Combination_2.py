class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result=[]
        def backtrack(start,target,current):
            if target==0:
                result.append(list(current))
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                current.append(candidates[i])
                backtrack(i+1,target-candidates[i],current)
                current.pop()
        backtrack(0,target,[])
        return result
        