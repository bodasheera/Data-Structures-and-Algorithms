""" PROBLEM STATEMENT: Merge two sorted arrays with O(1) extra space

We are given two sorted arrays. We need to merge these two arrays such that the initial numbers (after complete sorting)
are in the first array and the remaining numbers are in the second array. Extra space is allowed in O(1).

Example: 

Input: ar1[] = {10};
       ar2[] = {2, 3};
Output: ar1[] = {2}
        ar2[] = {3, 10}  

Input: ar1[] = {1, 5, 9, 10, 15, 20};
       ar2[] = {2, 3, 8, 13};
Output: ar1[] = {1, 2, 3, 5, 8, 9}
        ar2[] = {10, 13, 15, 20}

"""


"""
SOLUTION

Brute Force

1. use new array to store all elements from first and second list 
2. sort data in new array
3. copy first n elements in array1
4. copy next m elements in array 2

Time Complexity : O(N) + O(NlogN) + O(N) (putting in new array , sorting , putting it back to 2 arrays)
Space Complexity: O(N)

Solution 2 : O(m*n)

Since both the arrays are sorted take advantage of it 

1. loop through first array 
2. check a[i] with first element of second array
3. swap if a[i] > b[0]
4. now fix second array by insertion sort method (inserting a element in sorted array)

Time Complexity : O(n*m)
Space Complexity: O(1)

Solution 3 : GAP Algo

Basically find gap which is half array size . then 2 pointers of width gap
then increment and swap it if greater till end of array 
keep reducing gap by half till gap is 1 

1. gap = ceil( N/ 2)
2. while gap > 0 and j < n
3. i = 0, j = gap 
4. if a[i] > a[j] swap it 
5. i++, j++
6. gap = ceil(gap/2)

Time Complexity : O(logn * n)

"""

from math import ceil
from typing import List


class BruteForce:
    
    #Function to merge the arrays.
    def merge(self,arr1: List,arr2: List ,n,m):
        
        temp_arr = arr1 + arr2
        temp_arr.sort()

        arr1 = [temp_arr[i] for i in range(n)]
        arr2 = [temp_arr[i] for i in range(n, m+n)]


class Optimized1:

    #Function to merge the arrays.
    def merge(self,arr1: List,arr2: List ,n,m):
        
        # loop thru first array
        for i in range(0,n):

            # check if second array's first element is smaller than a[i] then swap
            if(arr1[i] > arr2[0]):
                temp = arr1[i]
                arr1[i] = arr2[0]
                arr2[0] = temp 

                # make the second array sorted
                if(arr2[0]>arr2[1]):
                    for j in range(0,m-1):
                        if arr2[j] >= arr2[j+1]:
                            temp = arr2[j]
                            arr2[j] = arr2[j+1]
                            arr2[j+1] = temp 

                

class GAP_Algo:


    def get_element(self,arr1,arr2,n, index):

        if index <= n -1 :
            return 0, index
        else :
            return 1, index - n - 1


    #Function to merge the arrays.
    def merge(self,arr1: List,arr2: List ,n,m):
        
        gap = ceil((m+n) / 2)
        i = 0
        j = gap 


        while gap >= 1 and j < m+n :

                
            if a > b:
                temp = self.get_element(arr1,arr2,n,i) 
                a= b
                b = temp 

                i+=1
                j+=1
                
        print(arr1, arr2)

GAP_Algo().merge([1 ,3 ,5 ,7],[0 ,2 ,6 ,8 ,9], 4, 5)