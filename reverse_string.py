class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        reversedwords=' '.join(reversed(words))
        return reversedwords