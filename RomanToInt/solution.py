class Solution(object):
    def romanToInt(self, s):
        data = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            "IV":4,
            "IX":10,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")
        result = 0
        for roman in s:
            result += data.get(roman)
        return result
    
result = Solution()
# result.romanToInt("MCMXCIV")