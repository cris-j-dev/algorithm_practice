"""
217. Contains Duplicate
Difficulty:Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for n in nums:
            if n not in hash_table:
                hash_table[n] = True
            else:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    # print(solution.containsDuplicate(nums=[1, 2, 3, 1]))  # true
    print(solution.containsDuplicate(nums=[1, 2, 3, 4]))  # false
    # print(solution.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # true
