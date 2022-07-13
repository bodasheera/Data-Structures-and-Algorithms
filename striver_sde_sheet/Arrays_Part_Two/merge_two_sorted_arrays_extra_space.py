""" PROBLEM STATEMENT: Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should 
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result 
can fit in nums1.

"""


"""
SOLUTION

Brute Force

1. if m == 0 return num2
2. else if n == 0 return num1
3. else
4. create i and j as zero and new empty array
5. create a while loop to see if i is less than m and j is less than n
6. check num1[i] and num2[j] as see which is lower . 
7. push lower val to new arr and increment iterator of lower value
8. if i is less than num1 then append remaining num1 to arr
9. if j is less than num2 then append remaining num2 to arr

Time Complexity : O(m*n)
Space Complexity : O(m+n)
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if m == 0:
            nums1 = nums2

        elif n == 0:
            pass
        else :
            i = j = 0
            temp = nums1[0]
            while(i < m or j< n):

                if temp <= nums2[j] and i < m:
                    i+=1
                    temp = nums1[i]
                elif i >= m and temp <= nums2[j]:
                    nums1[i] = temp 
                    temp = nums2[j]
                    j+=1
                    i+=1

                elif temp >= nums2[j]:
                    temp = nums1[i]
                    nums1[i] = nums2[j]
                    j+=1 
                    i+=1
        nums1[-1] = temp
        return nums1


test = Solution()
res = test.merge([1,2,3,0,0,0],3,[2,5,6],3)
print(res)