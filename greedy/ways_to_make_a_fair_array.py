"""
1664. Ways to Make a Fair Array
Medium

You are given an integer array nums. You can choose exactly one index (0-indexed) and remove the element. Notice that the index of the elements may change after the removal.

For example, if nums = [6,1,7,4,1]:

Choosing to remove index 1 results in nums = [6,7,4,1].
Choosing to remove index 2 results in nums = [6,1,4,1].
Choosing to remove index 4 results in nums = [6,1,7,4].
An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.

Return the number of indices that you could choose such that after the removal, nums is fair.

 

Example 1:

Input: nums = [2,1,6,4]
Output: 1
Explanation:
Remove index 0: [1,6,4] -> Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
Remove index 1: [2,6,4] -> Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
Remove index 2: [2,1,4] -> Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
Remove index 3: [2,1,6] -> Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
There is 1 index that you can remove to make nums fair.
Example 2:

Input: nums = [1,1,1]
Output: 3
Explanation: You can remove any index and the remaining array is fair.
Example 3:

Input: nums = [1,2,3]
Output: 0
Explanation: You cannot make a fair array after removing any index.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
"""

from typing import List
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd = even = 0
        even = sum(nums[::2])
        odd = sum(nums[1::2])

        prev_odd = prev_even = 0
        count = 0
        for i in range(len(nums)):
            if i % 2 == 1:
                curr_even = odd - prev_odd - nums[i] + prev_even
                curr_odd = even - prev_even + prev_odd
                prev_odd += nums[i]
            else:
                curr_even = prev_even+odd-prev_odd
                curr_odd = prev_odd+even-nums[i]-prev_even
                prev_even += nums[i]
            if curr_even == curr_odd:
                count += 1

            print(curr_even)
            print(curr_odd)
            print("=====================")
        return count
if __name__ == "__main__":
  solution = Solution()
  # print(solution.waysToMakeFair(nums=[2,1,6,4])) # 1
  # print(solution.waysToMakeFair(nums=[1,1,1])) # 3
  # print(solution.waysToMakeFair(nums=[1,2,3])) # 0
  print(solution.waysToMakeFair(nums=[4,5,2,2,1,1,4,4,5,3,2,3,5,3,2,1,2,1,1,3,3,3,5,1,1,2,3])) # 1