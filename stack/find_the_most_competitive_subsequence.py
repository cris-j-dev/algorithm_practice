"""
1673. Find the Most Competitive Subsequence
difficult:Medium

Share
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

 

Example 1:

Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
Example 2:

Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= nums.length
"""

from typing import List
class Solution:
  def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
    # ret = []
    # nums.append(0)
    # idx = 0
    # for i in range(k, 0, -1):
    #   if k == len(nums)-1:
    #     return ret+nums[:-1]
    #   value = min(nums[idx:-i])
    #   idx = idx+nums[idx:-i].index(value)+1
    #   ret.append(value)

    # return ret
    ret = []
        
    for i in range(len(nums)):
      while ret and nums[i] < ret[-1] and len(ret)-1+len(nums)-i >= k:
        ret.pop()
      if len(ret) < k:
        ret.append(nums[i])
            
    return ret

if __name__ == "__main__":
  solution = Solution()
  print(solution.mostCompetitive(nums=[2,4,3,3,5,4,9,6], k=4)) # [2,3,3,4]
  # print(solution.mostCompetitive(nums=[3,5,2,6] , k=2)) # [2,6]
  # print(solution.mostCompetitive(nums=[0]*10**9 , k=50000)) # [2,6]
