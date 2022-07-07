""" PROBLEM STATEMENT: next_permutation

Given an array Arr[] of integers, rearrange the numbers of the given array into the 
lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible 
order (i.e., sorted in ascending order).

Example 1:
Input format: Arr[] = {1,3,2}

Output: Arr[] = {2,1,3}

Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,1 , 3} , {2,3,1} , {3,1,2} , {3,2,1}}. 
So, the next permutation just after {1,3,2} is {2,1,3}.

Example 2:

Input format: Arr[] = {3,2,1}

Output: Arr[] = {1,2,3}

Explanation: As we see all permutations of {1,2,3}, we find {3,2,1} at the last position. 
So, we have to return the topmost permutation.
    
    
"""

"""
Solution 1 

{1,3 ,2 }

    3
  1   2  (increasing left to right)

  1. always there is nums[i] increasing sequence left to right (even if one element)
  2. traverse backwards and find index where increasing order breaks
  3. i = 0 as 1 < 3 
  4. since its next permutation we need something greater that nums[i][i] and next greater value 
  5. since its reverse increasing traverse backwards till nums[i][j] > nums[i][i]
  6. j = 2 as 2 > 1 
  7. now swap values at i and j
  8. 2 3 1 
  9. 3 1 is remaining substring and in next permutation we need least rank value 
  10. since its increasing backwards we can swap it to get least rank 
  11. 2 1 3


"""

from typing import List
from numpy import swapaxes
class Solution:

    def swap(self, nums, i, j):
        nums[i] = nums[i] + nums[j]
        nums[j] = nums[i] - nums[j]
        nums[i] = nums[i] - nums[j]

    def reverse(self, nums, i, j):
        while(i < j):
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # find i (increasing sequence breaks)

        i = len(nums) - 2

        # find where increasing order breaks
        while(i >= 0 and nums[i] >= nums[i+1]):
            i-=1

        if(i >= 0):
            j = len(nums) - 1

            # find next increasing value for
            while(nums[i] >= nums[j]):
                j = j-1

            self.swap(nums, i, j)

        self.reverse(nums, i+1, len(nums)-1)

