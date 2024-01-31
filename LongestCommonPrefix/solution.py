class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""
        final_result = ""
        first_str = strs[0]
        
        if len(strs) == 0:
            return result
        
        for a in range(len(first_str)):
            is_exist = 0
            for str in strs:
                if first_str[:a+1] == str[:a+1]:
                    is_exist += 1
            if is_exist == len(strs):
                result = first_str[:a+1]
        return result

result = Solution()