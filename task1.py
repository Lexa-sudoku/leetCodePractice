''' TASK
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
class Solution:
    def twoSum(self,nums: List[int],target:int)->List[int]:
        known={}
        for idx,num in enumerate(nums):
            a = target - num
            if a in known:
                return[known[a],idx]
            known[num]=idx


'''The twoSum function finds two numbers in a list that add up to a given target. It uses a dictionary to track numbers seen so far and their indices.

For each number in the list:
It calculates the complement needed to reach the target.
If the complement is already in the dictionary, it returns the indices of both numbers.
Otherwise, it adds the current number and its index to the dictionary.

This approach ensures a single-pass solution with O(n) time complexity.'''