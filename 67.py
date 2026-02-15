class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA+digitB+carry
            char = str(total%2)
            res = char+res
            carry = total//2

        if carry:
            res = "1" + res

        return res

if __name__ == "__main__":
    a = "0110"
    b = "1011"
    s = Solution()
    res = s.addBinary(a, b)
    print(res)

