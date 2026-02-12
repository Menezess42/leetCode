from collections import defaultdict

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            count_dict = defaultdict(int)
            for j in range(i, n):
                count_dict[s[j]] += 1
                if len(set(count_dict.values())) == 1:
                    res = max(res, j-i+1)

        return res
