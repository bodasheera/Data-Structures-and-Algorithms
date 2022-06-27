""" PROBLEM STATEMENT: PASCALS TRIAMGLE

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
    Input: numRows = 1
    Output: [[1]]

Constraints:
    1 <= numRows <= 30
"""





from typing import List


class Solution:
        
    def generate(self, numRows: int) -> List[List[int]]:

        output = []

        if numRows >= 1:
            output.append([1])
        if numRows >= 2:
            output.append([1,1])
        if numRows >= 3 :
            for i in range(2,numRows):
                temp = [1]
                prev = output[i-1]

                for j in range(i-1):
                    temp.append( prev[j] + prev[j+1] )
                temp.append(1)
                output.append(temp)

        return output


test = Solution()
print(test.generate(4))