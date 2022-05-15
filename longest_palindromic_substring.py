"""
5. Longest Palindromic Substring
Difficulty:Medium

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_value = s[0]
        count = 1
        left = []
        right = []
        for mid_index in range(1, len(s) + 1):
            if mid_index - count >= 0 and mid_index + count < len(s):
                if s[mid_index - count] == s[mid_index + count]:
                    left.append(s[mid_index - count])
                    right.append(s[mid_index + count])
                    count += 1
                else:
                    res_value = "".join(left) + s[mid_index] + "".join(right)
                    left.clear()
                    right.clear()

        return res_value


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome(s="babad"))  # "bab" or "aba"
    print(solution.longestPalindrome(s="cbbd"))  # "bb"
    print(solution.longestPalindrome(s="abb"))  # "bb"
    print(solution.longestPalindrome(s="aacabdkacaa"))  # "aca"
