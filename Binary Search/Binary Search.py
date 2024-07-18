from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left ,right = 0,len(nums) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if target > nums[mid] :
                left = mid + 1
            elif target < nums[mid] :
                right = mid - 1
            else:
                return mid
        return -1 


#Example

x = Solution()
nums = [-1,0,2,4,6,8]
target = 3

print(x.search(nums,target))
