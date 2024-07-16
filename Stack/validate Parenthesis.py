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
        return True if not x else False


#Example:
s = "([{}])"
x = Solution()
print(x.isValid(s))
