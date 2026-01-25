class Solution:
    def intToRoman(self, num: int) -> str:
        symRom = [["I", 1],["IV", 4],["V", 5],
                   ["IX", 9],["X", 10],["XL", 40],
                   ["L", 50],["XC", 90],["C", 100],
                   ["CD", 400],["D", 500],["CM", 900],["M", 1000],]
        response = ""
        for sym, val in reversed(symRom):
            count = num//val
            if count:
                response+=(sym*count)
                num=num%val
        return response

if __name__ == '__main__':
    s = Solution()
    r = s.intToRoman(1994)
    print(r)
