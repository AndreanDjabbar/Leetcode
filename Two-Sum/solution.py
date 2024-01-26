class Solution(object):
    def twoSum(self, nums, target):
        for a in range(0, len(nums)):
            is_continue = True
            first_index = a

            for b in range(a+1, len(nums)):
                second_index = b

                if nums[first_index] + nums[second_index] == target:
                    is_continue = False
                    return [first_index, second_index]
            
            if is_continue == False:
                break
answer = Solution()
result = answer.twoSum([3, 2, 4], 6)
print(result)