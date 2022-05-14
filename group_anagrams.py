"""
49. Group Anagrams
Difficulty:Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for word in strs:
            new_word = "".join(sorted(word))
            if new_word in hash_table.keys():
                hash_table[new_word].append(word)
            else:
                hash_table[new_word] = [word]

        return hash_table.values()


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
    )  # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(solution.groupAnagrams(strs=[""]))  # [[""]]
    print(solution.groupAnagrams(strs=["a"]))  # [["a"]]
