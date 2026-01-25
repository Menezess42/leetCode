class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V": 5, "X": 10,"L":50, "C": 100, "D": 500, "M":1000}
        s_size = len(s)
        result = 0
        for i in range(s_size):
            if i+1<s_size and roman[s[i]] < roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result+=roman[s[i]]
        return result


if __name__ == '__main__':
    s = Solution()
    number = input('...: ')
    while len(number) > 0:
        r = s.romanToInt(number)
        print(r)
        number = input('...: ')
