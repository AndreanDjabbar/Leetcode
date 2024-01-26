class Solution(object):
    def isPalindrome(self, x):
        # str_num = str(x)
        # str_len = len(str_num)
        # num = x
        # result = 0
        
        # multiplier = 10 ** (str_len - 1)
        # while num != 0:
        #     current_num = num % 10
        #     result = result + (current_num * multiplier)
        #     num = int(num / 10)
        #     multiplier = multiplier / 10
        # result = int(result)
        # if result == x:
        #     return True
        # else:
        #     return False


        num_str = str(x)
        nums = num_str[-1::-1]
        if nums == str(x):
            return True
        else:
            return False