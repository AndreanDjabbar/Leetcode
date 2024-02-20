class Solution(object):
    def removeDuplicates(self, nums):
        nums_copy = [num for num in nums]
        # Declare nums_copy with a value of nums
        inventory = []
        # Declare inventory as a empty list
        for num in nums_copy:
            # Loop for every element(num) in nums
            if num not in inventory:
                # 
                inventory.append(num)
                # add element with value = num to inventory
            else:
                nums.remove(num)
                # Remove element with value = num from nums
        k = len(nums)
        # Declare k as a length of nums
        return k
        # return k for a final result
        
result = Solution()
# Declare result as a object of class Solution
print(result.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
