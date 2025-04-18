'''
TASK

Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed = 0
        while reversed<x:
            reversed = reversed * 10 + x % 10
            x=x//10
        return reversed == x or reversed // 10 == x

'''
Algorithm

Checks if an integer is a palindrome without converting it to a string.
It reverses half of the number and compares it to the other half.

If the number is negative or ends with 0 (but isn't 0), it's not a palindrome.

Builds reversed from the last digits of x until reversed >= x.

Returns True if the reversed half equals the remaining half (handling both even and odd digit counts).
'''