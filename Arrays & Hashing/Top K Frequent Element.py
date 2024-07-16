from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = []
        temp = []
        for i in nums:
            temp.append(nums.count(i))
        temp = sorted(list(set(temp)))
        for j in nums:
            for i in range(len(nums)):
                if temp and nums.count(nums[i]) == temp[-1] and nums[i] not in final:
                    final.append(nums[i])
                if len(final) == k:
                    return final
            temp.pop()

        
        
#Example

nums = [1,2,2,3,3,3]
nums=[1,2]
k = 2
x = Solution()
print(x.topKFrequent(nums,k))
