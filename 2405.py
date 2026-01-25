class Solution:
    def partitionString(self, s: str) -> int:
        currSet = set()
        response = 1
        for c in s:
            if c in currSet:
                response += 1
                currSet = set()
            currSet.add(c)

        return response


if __name__ == '__main__':
    s = Solution()
    print(s.partitionString('abacaba'))
