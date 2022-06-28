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


3 questions can be asked by interviewer 
1. print entire pascal triangle 
2. print pascal value at nth row and cth column 
3. print pascal row at n 


Observations 
1. first and last value of row is always 1
2. each row has always columns of length of row number (1st row 1 column , 2nd row 2 columns .....)
3. element is sum of values of 2 elements of above row


Print entire pascal triangle 
Time Complexity : O(N**2) N to traverse rows . N to traverse column
Space Complexity : O(N**2) to store 2d matrix 
"""



from typing import List


class SimpleSolution:
        
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
        


class Solution2:
        
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = [0] * numRows; # pascal triagle of length n rows

        for i in range(0, numRows):
            triangle[i] = [0] * (i+1) # column length will be row number

            triangle[i][0] = triangle[i][-1] = 1 # first ele and last ele will be 1

            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j - 1] + triangle[i-1][j]

        return triangle
        

test = Solution2()
print(test.generate(4))