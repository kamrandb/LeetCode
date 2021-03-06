'''
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = ""
        temp = ""
        for char in s:
            if char not in temp:
                temp += char
            else:
                if len(temp) > len(longest):
                    longest = temp
                    temp = temp[temp.index(char)+1:]+char
                else:
                    temp = temp[temp.index(char)+1:]+char
        if len(temp) > len(longest):
            return len(temp)
        return len(longest)

#second solution:
    def lengthOfLongestSubstring2(self, s):
        res = ""
        temp = ""
        for char in s:
            if char not in temp:
                temp += char
            else:
                temp = temp[temp.index(char)+1:]+char
            if len(temp) > len(res):
                res = temp
        return len(res)




if __name__ == "__main__":
    a = Solution()
    print(a.lengthOfLongestSubstring("bpfbhmipx"))
