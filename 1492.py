import math
class Solution:
    def kthFactor(self, n: int, k: int)-> int:
        big, small = [], []
        for num in range(1, int(math.sqrt(n))+1):
            if n%num == 0:
                divResult = n//num
                print(f"div:{divResult} num:{num}")
                small.append(num)
                if num!=divResult:
                    big.append(divResult)
        big.reverse()
        print(f"small:{small}")
        print(f"big:{big}")
        merged = small+big
        print(f"mergeList:{merged}")
        if len(merged)<k:
            return -1
        return merged[k-1]

if __name__ == '__main__':
    s = Solution()
    while True:
        n = int(input('N: '))
        k = int(input('K: '))
        if k==-1:
            break
        r = s.kthFactor(n, k)
        print(f"Response: {r}")

