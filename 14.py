import time
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            print(f"i: {i}")
            for s in strs:
                print(f"{s}")
                print(f"s[i]: {s[i]}")
                if i==len(s) or s[i]== strs[0][i]:
                    print(f"strs[0][i]: {strs[0][i]}")
                if i==len(s) or s[i]!= strs[0][i]:
                    print(f"strs[0][i]: {strs[0][i]}")
                    return res
                time.sleep(2)
            res += strs[0][i]

        return res

if __name__=='__main__':
    s = Solution()
    r = s.longestCommonPrefix(["flower", "flow", "flight"])
    print(r)
    time.sleep(5)
    r = s.longestCommonPrefix(["dog", "racecar", "car"])
    print(r)
    time.sleep(5)
    r = s.longestCommonPrefix(["flower", "flower", "car"])
    print(r)
