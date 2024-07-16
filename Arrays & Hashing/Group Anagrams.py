from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}
        for i in strs:
            j = "".join(sorted(i))
            if j not in x:
                x[j] = []
            x[j].append(i)
        result = list(x.values())
        return result


#Example

strs = ["act","pots","tops","cat","stop","hat"]
a = Solution()
print(a.groupAnagrams(strs))
