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

--------------------------------------------

Print pascal value at nth row and cth column 

Binomial theoram formula (n-1)C(r-1)

nCr = n!/(r!(n-r)!) 

Time Complexity : O(N) - For Finding Factorial
Space Complexity: O(1) 

--------------------------------------------

Print pascals row when rowNum is given 

1.Use pascals formula for each element in row 
2. row will have rowNum elements 

Approach one 
1. use binomial theoram formula and find value for each element 

Time Complexity : o(N*N) -> factorial for each element and loop
Space Complexity: O(N) -> store pascal row 

Approach Two 
2. find factorial for all elements using pattern approach in O(1) . 

rowNum = 5 
formula n-1Cr-1

4C0 = 1
4C1 = 1 * (4 / 1) # 4 is 5 -1 ie rowNum - i , 1 is i 
4C2 = 4 * (3 / 2) = 6
4C3 = 6 * (2 / 3) = 4 
4C4 = 4 * (1 / 4) = 0


formula is SUM OF ALL prev * ((rowNum - i) / i)


Time Complexity : O(N) -> looping for all elements 
Space Complexity: O(N) -> store pascal row 

"""



from math import factorial
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
        


class PascalTriangleOptimised:
        
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = [0] * numRows; # pascal triagle of length n rows

        for i in range(0, numRows):
            triangle[i] = [0] * (i+1) # column length will be row number

            triangle[i][0] = triangle[i][-1] = 1 # first ele and last ele will be 1

            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j - 1] + triangle[i-1][j]

        return triangle
        

class PascalElement:

    def __factorial(self, n):

        if n == 1:
            return 1
        else:
            return n * self.__factorial(n-1) 

    def generate(self , row: int, col: int) -> int:
        
        n = row - 1
        r = col - 1
        return int(factorial(n) / (factorial(r) * factorial(n-r)))



class PascalRowSimple:

    def __factorial(self, n):

        if n == 1:
            return 1
        else:
            return n * self.__factorial(n-1) 

    def generate(self , rowNum: int) -> int:
        
        row = [0]* rowNum 
        row[0] = row[-1] = 1

        n = rowNum - 1 

        for i in range(1, rowNum -1):
            row[i] = int(factorial(n) / (factorial(i) * factorial(n-i)))
            
        return row


class PascalRowOptimized:

    def generate(self ,numRows) -> List[int] :

        arr = [0]*numRows # column of length row 

        prev = 1
        arr[0] = prev

        for i in range(1 , numRows):
            prev = int(prev * ((numRows-i)/i))
            arr[i] = prev

        return arr

test = PascalRowOptimized()
print(test.generate(6))