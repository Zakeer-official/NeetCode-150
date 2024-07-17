from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = int("".join(map(str,digits))) + 1
        return [int(i) for i in str(x)]


#Example

digits = [1,2,3,4]
a = Solution()
print(a.plusOne(digits))
