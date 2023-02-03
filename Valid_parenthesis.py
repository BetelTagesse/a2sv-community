class Solution:
    def isValid(self, s: str) -> bool:
        k={')':'(',']':'[','}':'{'}
        stack=[]
        for c in s:
            if c in k:
                if stack and stack[-1]==k[c]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)
        if stack==[]:
            return True
        else:
            return False