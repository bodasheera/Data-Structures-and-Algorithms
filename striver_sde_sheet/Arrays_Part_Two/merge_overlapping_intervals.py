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

Ask interviewer if input is sorted (Very Imp)

brute force
1. sort the array in descending order
2. how can 2 list overlap . simple 

Scenario 1 

start1                     end1
----------------------------
                     ----------------------
                     start2               end2

start1 <= start2 <= end1
end1 <= end2


Scenario 2 

start1                                      end1
---------------------------------------------
                 -----------------
                 start2           end2

start1 <= start2 <= end1
end2 <= end1

Time Complexity : O(nlogn) + O(n) + O(n) = O(nlogn)
sort array + merge overlapping + remove None

Space Complexity = O(N)
3. now loop the list and figure out which case it is 
4, if case 1 then new value is [start1, end2]
5. if case 2 then new value is [start1, end1]

6. make arr[i+1] as new value and make arr[i] as None 
7. now remove None and return final result

Time Complexity : O(nlogn) + O(n) + O(n) = O(nlogn)
sort array + merge overlapping + remove None

Space Complexity = O(N) remove None from Array


Optimize code (same time and space complexity as above code but cleaner solution)
1. use temp variable to store first element and create a new array to store overlapped values
2. loop through list and see if current element overlaps with temp 
3. if temp and current value overlaps then update temp to new overlapped value and increment i
4. if temp and current value dont overlap then add temp to new array and update temp as cuurent value and increment i
5. when u reach end of loop add temp to new array

Time Complexity : O(nlogn) + O(n)
Space Complexity : O(n)
"""




from cgitb import reset
from typing import List
class BruteForce:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        N = len(intervals)

        if N == 1:
            return intervals

        # sort the array
        intervals.sort(key=lambda l: l[0], reverse=False)

        for i in range(len(intervals)-1):
            if intervals[i]:
                start1 = intervals[i][0]
                end1 = intervals[i][1]
                start2 = intervals[i+1][0]
                end2 = intervals[i+1][1]

                if(start2 >= start1 and start2 <= end1):
                    if (end2 >= end1):
                        intervals[i+1] = [start1, end2]

                    elif (end1 >= end2):
                        intervals[i+1] = [start1, end1]
                    intervals[i] = None

        return [x for x in intervals if x is not None]


class Optimal:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        result = []

        # sort the array
        intervals.sort(key=lambda l: l[0], reverse=False)

        tempInterval = intervals[0]

        for it in intervals:

            # check if overlapping
            if(it[0] <= tempInterval[1]):
                tempInterval[1] = max(it[1], tempInterval[1])
            else:
                result.append(tempInterval)
                tempInterval = it

        # at end put temp interval to result
        result.append(tempInterval)

        return result
