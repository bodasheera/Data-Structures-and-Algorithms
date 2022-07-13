"""
Bubble sort 

The largest element bubbles to the end of the array after each pass
so number of loops is N-1 
IF N = 5 THEN 4 LOOPS

and the number of comparisons in each loop decreases by 1 as largest element is already at the end of the array
so N-1 -i comparisons in each loop 
example :
5 9 2 7 1

step 1: 5 2 7 1 9 (9 bubbled to the right and 4 comparisons)
step 2: 2 5 1 7 9 (7 bubbled to the right and 3 comparisons)
step 3: 2 1 5 7 9 (5 bubbled to the right and 2 comparisons) 
step 4: 1 2 5 7 9 (2 bubbled to the right and 1 comparison)

Time Complexity : O(N*N)  N for number of passes and N for comparison
Space Complexity : O(1) because array is updated in place
"""


from typing import List


class BubbleSort:

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def sort(self, arr: List) -> List:
        N = len(arr)
        for i in range(N-1):
            for j in range(N-1-i):
                if(arr[j] > arr[j+1]):
                    self.swap(arr, j, j + 1)
        return arr
