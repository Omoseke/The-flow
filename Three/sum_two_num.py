class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Dictionary to store number and its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return None  # In case there's no solution (not expected as per the problem)
solver = Solution()

# Test cases
print("Test Case 1:")
print(solver.twoSum([2, 7, 11, 15], 9))
