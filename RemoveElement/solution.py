class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)
    
result = Solution()
nums = [0,1,2,2,3,0,4,2]
target = 2
final_result = result.removeElement(nums, target)