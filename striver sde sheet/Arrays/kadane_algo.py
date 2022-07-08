""" PROBLEM STATEMENT: Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
    Input: nums = [1]
    Output: 1

Constraints:
    1 <= nums.length <= 10**5
    -10**4 <= nums[i] <= 10**4
"""


"""
Brute Force

traverse i = 0 to n-1
    sum = -1
    traverse j = i to n-1
        sum = sum + A[j]

        if sum > max
            max = sum 

return max


Time Complexity : O(N**2)
Space Complexity : O(1)


Approach 2 in O(n) time - Kadane Algo

1. sum = 0, max = nums[0] first element
2. traverse the array
3. sum = sum + nums[i]
4. if sum > max then max = sum 
5. if sum is negative then sum is zero (why to add negative value to sum . we need max sum so reset to zero)
6. traverse full array and return max

"""


from typing import List


class BruteForce:

    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            max = -10**5
            for i in range(0, len(nums)):
                sum = 0
                for j in range(i , len(nums)):
                    sum+=nums[j]
                    if (sum > max):
                        max = sum
            return max



class OptimalSolution:

    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0 ; max = nums[0] 

        for i in range(0, len(nums)):
            sum = sum + nums[i]

            if sum > max:
                max = sum 

            if sum < 0:
                sum = 0

        return max

