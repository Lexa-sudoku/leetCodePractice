''' TASK
Given a string s, find the length of the longest substring without duplicate characters 

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len
    

'''The lengthOfLongestSubstring function finds the length of the longest substring without repeating characters.
It uses a sliding window with two pointers (left and right) and a set to track seen characters.

For each character:

If it's already in the set, move the left pointer forward and remove characters until the duplicate is gone.

Add the current character to the set.

Update the maximum length found so far.

This gives an efficient O(n) time solution, where n is the length of the string.'''