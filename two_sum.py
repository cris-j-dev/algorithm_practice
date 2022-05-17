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
    def twoSum2(self, nums: List[int], target: int) -> List[int]:

        start = 0
        res = 0
        for num_idx in range(0, len(nums) + 1):
            start += 1
            for i in range(start, len(nums)):
                res = nums[num_idx] + nums[i]
                if res == target:
                    return [num_idx, i]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for idx, num in enumerate(nums):
            print("index_map : ", index_map)
            rem = target - num
            if rem in index_map:
                return index_map[rem], idx
            else:
                index_map[num] = idx


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(nums=[2, 7, 11, 15], target=9))  # [0, 1]
    print(solution.twoSum(nums=[3, 2, 4], target=6))  # [1, 2]
    print(solution.twoSum(nums=[3, 3], target=6))  # [0, 1]
    print(solution.twoSum(nums=[0, 4, 3, 0], target=0))  # [0, 3]
    print(solution.twoSum(nums=[-1, -2, -3, -4, -5], target=-8))  # [2, 4]
