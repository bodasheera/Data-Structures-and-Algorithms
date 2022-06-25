""" PROBLEM STATEMENT: SET MATRIX ZERO

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

Example 1:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2**31 <= matrix[i][j] <= (2**31) - 1

"""

""" PSEUDO CODE SOLUTION

SIMPLE APPROACH:
    1. loop through matrix
    2. store row and col indices as tuple in array where val is zero
    3. loop through indices array 
        1. row logic - loop thru matrix total col length and set row-col val to zero
        2. col logic - loop thru matrix total row length and set row-col val to zero

    Time Complexity 
        O( m*n + (l* (m + n)) )
        m*n -> find indices 
        l * (m + n) -> update matrix where l is total indexes where val is zero 

    Space complexity 
        O(l) -> index matrix

BRUTE FORCE:
    Ask interviewer if only positive integers are allowed
    1. loop through matrix 
    2. if element is zero then set entire row and entire col to -1 (any number which cant be part to matrix)
       except zero because zero can be part of another row-col where we need to update values
    3. loop through matrix again and replace all -1 with zero  

    Time Complexity 
        O( m*n(m + n) + m*n )    

    Space Complexity
        O(1) -> same matrix used 
"""

# Simple Approach
    
from array import array
from typing import List

class Solution:

    index_matrix: array

    def setZeroes(self, matrix: List[List[int]]) -> None:

        self.set_index_matrix(matrix)

        if(len(self.index_matrix) == 0):
            return matrix
        else:
            return self.updated_matrix(matrix)


    def set_index_matrix(self, matrix):
        self.index_matrix = []

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if (val == 0):
                    self.index_matrix.append((i, j))


    def updated_matrix(self, matrix):
        
        total_cols = len(matrix[0])
        total_rows = len(matrix)

        for i in self.index_matrix:
            row = i[0]
            col = i[1]

            # row logic
            for col_index in range(total_cols):
                matrix[row][col_index] = 0

            # col logic
            for row_index in range(total_rows):
                matrix[row_index][col] = 0

        return matrix

test = Solution()

print(test.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(test.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))



# Brute Force

class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        for i , row in enumerate(matrix):
            for j, val in enumerate(row):

                if(val == 0):
                    pass 
                
                    # row logic 

                    # col logic 
