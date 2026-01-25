from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1 
            while l<r:
                sum = a+nums[l]+nums[r]
                if abs(target - sum) < closest:
                    closest=sum
                if closest == target:
                    return closest
                if sum > target:
                    r -= 1
                else:
                    l += 1
        return closest 
    
if __name__ == '__main__':
    s  = Solution()
    r = s.threeSumClosest([9,-4,2,-1,-3,4,1],2)
    print(r)