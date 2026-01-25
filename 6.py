# n=1
# P-A-Y-P-A-L-I-S-H-I-R-I-N-G
# 0-1-2-3-4-5-6-7-8-9-1-1-2-3

# p---a---h---n
# a-p-l-s-i-i-g
# y---i---r----

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        print(f"Len of string: {n}")
        if numRows == 1 or numRows >= n:
            return s
        rows = [''] * numRows
        print(f"String matrix format: {rows}")
        cycle_len = 2 * (numRows - 1)
        print(f"Full Cycle 'V', where the code gos all the way down and up: {cycle_len}")
        for i in range(n):
            print(f"Walking in range of len of string: {i}")
            row = i % cycle_len
            print(f"row:{row}=i:{i}%cycle_len:{cycle_len}")
            if row < numRows:
                print(f"If row<numRows:{row}<{numRows}")
                rows[row] += s[i]
                print(f"rows[row] += s[i] <-> {rows[row]}+={s[i]}")
            else:
                rows[cycle_len - row] += s[i]
                print("else")
                print(f"rows[cycle_len-row]+=s[i] <-> {rows[cycle_len-row]} += {s[i]}")
            print("\n=============\n")
        return ''.join(rows)

if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 4
    result = sol.convert(s, numRows)
    print(result)

