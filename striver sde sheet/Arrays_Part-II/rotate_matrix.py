""" PROBLEM STATEMENT

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.


Example 1:

Input:  
[[1,2,3],
 [4,5,6],
 [7,8,9]]

Output: 
[[7,4,1],
 [8,5,2],
 [9,6,3]]

Example 2:

Input: 
[[5,1,9,11],
 [2,4,8,10],
 [13,3,6,7],
 [15,14,12,16]]

Output: 
[[15,13,2,5],
 [14,3,4,1],
 [12,6,8,9],
 [16,7,10,11]]

Constraints:
1. n == matrix.length == matrix[i].length
2. 1 <= n <= 20
3. -1000 <= matrix[i][j] <= 1000


Approach 1 : Use another matrix
Time Complexity = Space Complexity = O(n*n)

Approach 2 : 
1. Transpose Matrix -> row will be col and col will be row 
2. reverse all elements of every row 

the diagnol will be unaffected when you do transpose. 
so we need to swap row and cols only for lower triangle.
so we need triangle 2 loops i => 0 to N and j -> i to N for lower triangle

then loop every row and reverse it using 2 pointer approach start and end till start < end 

time complexity : O(N*N) + O(N*N) 
for transpose and for reversing 

space complexity : O(1) modified in place no new matrix used

"""

from typing import List


class BruteForce:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = C = len(matrix)
        data = [0] * R

        for i in range(R):
            data[i] = [0]*C

        for i in range(R):
            for j in range(C):
                data[j][i] =  matrix[R-1-i][j]
        
        matrix = data 


class Optimal:

    def swap(self, matrix ,j,i):
        temp = matrix[i]
        matrix[i] = matrix[j]
        matrix[j] = temp 

    def reverse(self, matrix,rowIndex, start, end):
        while(start < end):
                matrix[rowIndex][start], matrix[rowIndex][end] =  matrix[rowIndex][end], matrix[rowIndex][start]
                start+=1 ; end-=1

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        R = len(matrix) 
        C = len(matrix) 
        # transpose 
        for i in range(R):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        # reverse rows of array
        for i in range(R):
            self.reverse(matrix,i, 0,R-1)
            