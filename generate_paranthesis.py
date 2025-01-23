class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result =[]
        def backtrack(current,openn,close):
            if len(current)==2*n:
                result.append(current)
                return
            if openn<n:
                backtrack(current + "(",openn+1,close)
            if close<openn:
                backtrack(current+")",openn,close+1)
        backtrack("",0,0)
        return result