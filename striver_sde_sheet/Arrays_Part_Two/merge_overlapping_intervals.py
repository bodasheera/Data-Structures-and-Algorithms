""" PROBLEM STATEMENT
Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping interval

Example 1: 

Input: intervals=[[1,3],[2,6],[8,10],[15,18]]

Output: [[1,6],[8,10],[15,18]]

Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
 intervals.

Example 2:

Input: [[1,4],[4,5]]

Output: [[1,5]]

Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6] intervals.    

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

"""
brute force

"""


from sys import flags
from typing import List

from numpy import sort


class BruteForce:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        N = len(intervals)

        result = []

        # sort the array - bubble sort 

        return result


algo = BruteForce()
res = algo.merge([[1,3],[2,6],[8,10],[15,18]])
print(res)