class Solution:
    def isValid(self, s: str) -> bool:
        dic = { '}' : '{' , 
                ']' : '[' ,
                ')' : '('
              }
        x = []
        for i in s:
            if i in dic:
                if x and x[-1] == dic.get(i):
                    x.pop()
                else:
                    return False
            else:
                x.append(i)
        return len(x) == 0


#Example:
s = "([{}])"
x = Solution()
print(x.isValid(s))
