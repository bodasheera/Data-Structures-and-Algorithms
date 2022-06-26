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


APPROACH 3:
    Interviewer asks to reduce time complexity 

    1. create 2 new arrays row = [] and col = []
    2. loop through matrix
    3. if val is zero then store 0 in indexes for row and col : row[i]=0 and col[j] = 0
    4. loop through matrix again 
    5. if row[i] == 0 or col[j] == 0 set matrix[i][j] = 0

    or u can also use set instead of array and store indexes row.add(i) amd col.add(j)
    directly instead of 0 in i and j position 

    Time Complexity 
        O( m*n )    

    Space Complexity
        O( m + n ) -> 2 new arrays / sets


APPROACH 4:
    Optimized approach of approach 3 where first row and first column will be used as indexes instead
    of 2 new arrays

    1. col0 = 1 (tracker for matrix[0][0] as 00 common for both col and row array )
    2. loop through matrix 
    3. if val = 0 then matrix[i][0] = 0 and matrix[0][j] = 0 updated respective index arrays to 0 
    4. if val = 0 and j = 0 then col0 = 0 (because we cant make matrix[0][0] as 0 affects col and row)
    5. traverse array bottom to up and right to left 
    6. if matrix[i][0] = 0 or matrix[0][j] = 0 then matrix[i][j] = 0 
    7. if col0 is 0 then matrix[i][0] = 0

    Time Complexity 
        O(m*n)    

    Space Complexity
        O(1)


"""

# Simple Approach




from array import array
from typing import List
from sqlalchemy import true
class Solution1:

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


# Brute Force

class BruteForceSolution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):

                if(val == 0):
                    # row logic
                    for col_index in range(len(matrix[0])):
                        if(matrix[i][col_index] != 0):
                            matrix[i][col_index] = -100

                    # col logic
                    for row_index in range(len(matrix)):
                        if(matrix[row_index][j] != 0):
                            matrix[row_index][j] = -100

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if(val == -100):
                    matrix[i][j] = 0


# Reduced time complexity O(m*n) and space complexity O(m + n)

class Solution3:

    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = set()
        cols = set()

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):

                if(val == 0):
                    rows.add(i)
                    cols.add(j)

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):

                if(i in rows or j in cols):
                    matrix[i][j] = 0


# constant space complexity and O(mn) time complexity

class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:

        R = len(matrix)
        C = len(matrix[0])
        col0 = 1

        for i in range(R):
            if (matrix[i][0] == 0):
                col0 = 0
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        for i in range(R-1, -1, -1):
            for j in range(C-1, 0, -1):
                if (matrix[0][j] == 0 or matrix[i][0] == 0):
                    matrix[i][j] = 0

            if col0 == 0:
                matrix[i][0] = 0
