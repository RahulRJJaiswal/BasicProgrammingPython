"""
Approach - 1: Brute Force Approach
The brute force approach is a commonly used way to solve the problem. In this approach, our primary goal is to solve the problem, not efficiently. We check every possible pair and the number of possible pairs in the array. We will use the two for loop, add the two values, and compare the target value. If it is equal to the target value, return the indices of pairs of the integer.

Algorithm -

Run the first loop to point the first index of the solution in the array.
Run another loop to point a second index of the solution for every first integer.
If the both elements equal to the target value, return the both indices values
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

        return []


print(Solution().twoSum([2, 7, 11, 15], 9))
