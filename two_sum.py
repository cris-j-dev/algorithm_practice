"""
1. Two Sum
Difficulty:Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        start = 0
        res = 0
        for num_idx in range(0, len(nums) + 1):
            start += 1
            if nums[num_idx] < target:
                for i in range(start, len(nums) + 1):
                    res = nums[num_idx] + nums[i]
                    if res == target:
                        return [num_idx, i]


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(nums=[2, 7, 11, 15], target=9))  # [0, 1]
    print(solution.twoSum(nums=[3, 2, 4], target=6))  # [1, 2]
    print(solution.twoSum(nums=[3, 3], target=6))  # [0, 1]