from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

#Example

x = Solution()
nums = [1, 2, 3, 3]
print(x.hasDuplicate(nums))
