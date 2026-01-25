class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        num = 0
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        num *= sign
        if num < MIN_INT:
            return MIN_INT
        if num>MAX_INT:
            return MAX_INT
        return num


if __name__ == "__main__":
    s = Solution()
    r = s.myAtoi("    +0a32")
    print(r)
