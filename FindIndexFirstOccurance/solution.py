class Solution(object):
    def filter_element(self, haystack):
        element_stack = []
        indexs = []
        a = 0
        for element in haystack:
            if element == '_' and '_' not in element_stack:
                element_stack.append('_')
                indexs.append(a)
            elif element != '_' and '_' in element_stack:
                element_stack.pop()
            a += 1
        return indexs

    def strStr(self, haystack, needle):
        changer = '_' * len(needle)
        if needle in haystack:
            haystack = haystack.replace(needle, changer)
            result = self.filter_element(haystack)
            return result[0]
        else:
            return -1
        
result = Solution()
source = "leetcode"
target = "leeto"
final_result = result.strStr(source, target)