from typing import List


class Solution:
    def letterCombinations_iterative(self, digits: str) -> List[str]:
        if digits == "":
            return []
        r = [""]
        dictLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        for d in digits:
            newComb = []
            for comb in r:
                for l in dictLetter[d]:
                    newComb.append(comb + l)
            r = newComb

        return r

    def letterCombinations_recursive(self, digits: str) -> List[str]:
        if digits == "":
            return []
        r = []
        dictLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(pos, curStr):
            if len(curStr) == len(digits):
                r.append(curStr)
                return
            for c in dictLetter[digits[pos]]:
                dfs(pos+1, curStr+c)

        dfs(0, "")
        return r


if __name__ == "__main__":
    s = Solution()
    tests = ["2", "23", "234", "9876"]
    for digits in tests:
        r = s.letterCombinations_iterative(digits)
        print(r)

    for digits in tests:
        r = s.letterCombinations_iterative(digits)
        print(r)
