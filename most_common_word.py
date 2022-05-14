"""
819. Most Common Word
Difficulty:Easy

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"
 

Constraints:

1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
"""


from typing import List, OrderedDict
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r"[^a-zA-Z0-9 ]", " ", paragraph)

        hash_table = OrderedDict()
        max_word = None
        max_value = 0
        for word in paragraph.split():
            word = word.lower()
            if not word in banned:
                if not word in hash_table.keys():
                    hash_table[word] = 1
                else:
                    hash_table[word] += 1

                if hash_table[word] > max_value:
                    max_word = word
                    max_value = hash_table[word]
                # elif hash_table[word] == max_value:

        # return [
        #     k
        #     for k in sorted(hash_table.items(), key=lambda item: item[1], reverse=False)
        # ]
        return max_word


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.mostCommonWord(
            paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
            banned=["hit"],
        )
    )  # "ball"
    print(solution.mostCommonWord(paragraph="a.", banned=[]))  # "a"
    print(
        solution.mostCommonWord(paragraph="a, a, a, a, b,b,b,c, c", banned=["a"])
    )  # "b"
