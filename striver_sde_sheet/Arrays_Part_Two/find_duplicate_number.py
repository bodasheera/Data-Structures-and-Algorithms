""" PROBLEM STATEMENT: Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.


Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

"""

"""
Approach 1 : Brute Force 

for each element loop through all further elements and see if duplicate exists

Time Complexity: O(N*N)
Space Complexity : O(1)


Approach 2 : 
use gauss formula to find sum of n numbers (n(n+1))/2

[1,3,4,2,2] 
observe 1,2,3,4 is there and 2 is extra 

so if we can get sum of first 4 numbers and subtract from array sum we can get extra element


"""


from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)-1
        sum_of_n = int((n*(n+1))/2)

        sum = 0
        for i in nums:
            sum = sum + i

        return sum - sum_of_n

print(Solution().findDuplicate([3,1,3,4,2]))