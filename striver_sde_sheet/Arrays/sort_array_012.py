""" PROBLEM STATEMENT:  Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

Example 2:
    Input: nums = [2,0,1]
    Output: [0,1,2]

Constraints:
    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.

"""


"""

Approach 1 - sorting 
time complexity O(nlogn)
space complexity O(1)


Approach 2 - 2 passes 
1. count number of 0 ,1 ,2 in dictionary
2. traverse and replace array

time complexity O(n) + 3 O(n) => O(n)
space complexity O(1)


Approach 2 - Dutch National Flag Algorithm
1. low , mid , high 3 pointers
2. low and mid will be 0 and high will be N-1
3. left of low will be 0 and right of high will be 2 -> arr[0 to low- 1] will be 0 and arr[high+ 1 to N-1 ] will be 2
4. traverse array 
5. at any point mid will be 0 , 1 ,2 
6. if mid is zero -> swap(a[mid], a[low]) and mid ++ and low ++
7. if mid is 1 -> mid++
8. if mid is 2 -> swap(a[mid], a[high]) and high --

time complexity O(n)
space complexity O(1)
"""

from typing import List
class BruteForce:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        data = {"0": 0, "1": 0, "2": 0}
        for i in nums:
            data[str(i)] = data[str(i)] + 1

        nums = []
        for key in data.keys():

            num = int(key)

            for i in [num]*data[key]:
                nums.append(i)


class DutchNationalFlagAlgo:

    def swap(self, nums , a , b):
        temp = nums[a]
        nums[a]= nums[b]
        nums[b] = temp

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        mid = low = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                self.swap(nums, mid, low)
                mid += 1
                low += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                self.swap(nums, mid, high)
                high -= 1