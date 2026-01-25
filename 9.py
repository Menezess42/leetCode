class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_ = str(x)
        if len(x_)==1:
            return True
        aux = len(x_)
        if aux%2 == 1:
            x_ = x_[:aux//2]+x_[(aux//2)+1:]
        x_l = x_[:aux//2]
        x_r = x_[aux//2:]
        x_r = x_r[::-1]
        if x_l == x_r:
            return True
        return False





if __name__ == '__main__':
    c = Solution()
    r = int(input('Number: '))
    while r!=0:
        a = c.isPalindrome(r)
        print(a)
        r = int(input('Number: '))
