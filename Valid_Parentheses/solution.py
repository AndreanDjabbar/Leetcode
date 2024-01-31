class Solution(object):
    def isValid(self, s):
        data = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for element in s:
            if element in data:
                stack.append(element)
            elif len(stack) == 0 or element != data.get(stack.pop()):
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False
        

result = Solution()
result = result.isValid("{[]}{")

print(result)
