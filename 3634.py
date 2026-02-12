from typing import List


class Solution:
    def myInitialHypotese(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums) - 1
        count = 0
        while n > 0:
            if n == 0:
                return count
            elif k * nums[0] >= nums[n]:
                return count
            else:
                nums.pop(n)
                n -= 1
                count += 1
        return count

    def correctSolution(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = n
        right = 0
        for left in range(n):
            while right < n and nums[right] <= nums[left] * k:
                right += 1
                ans = min(ans, n - (right - left))

        return ans


if __name__ == "__main__":
    s = Solution()
    tests = [([2, 1, 5], 2), ([1, 6, 2, 9], 3), ([4, 6], 2)]
    for nums, k in tests:
        a = s.myInitialHypotese(nums, k)
        a = s.correctSolution(nums, k)
