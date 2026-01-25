class Solution:
    def longestPalindrome(s: str)-> str:
        subS=''
        if len(s)==1:
            return s
        def expandAroundCenter(left: int,right: int) -> str:
            while left>=0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        for i in range(len(s)):
            pal1 = expandAroundCenter(i,i)
            if(len(pal1)) > len(subS):
                subS=pal1

            pal2 = expandAroundCenter(i,i+1)
            if(len(pal2)) > len(subS):
                subS=pal2

        return subS

if __name__ == "__main__":
    s = Solution
    resposta = s.longestPalindrome("cbbd")
    print(resposta)
