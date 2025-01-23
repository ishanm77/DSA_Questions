class Solution(object):
    def beautySum(self, s):
        beauty=0
        n=len(s)
        for i in range(n):
            freq=defaultdict(int)
            for j in range(i,n):
                freq[s[j]] += 1
                freqs=list(freq.values())
                max_freq=max(freqs)
                min_freq=min(freqs)
                beautys=max_freq-min_freq
                beauty += beautys
        return beauty