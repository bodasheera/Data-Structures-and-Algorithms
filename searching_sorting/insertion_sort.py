"""INSERTION SORT

Intuition
Like sorting a pack of cards
You will be inserting a element in sorted array 
at every pass arr[0, i-1] will be already sorted

1. loop through array
2. for i check all previous value j
3. insert element in right position by comparing j and j-1 and swapping it if previous element is larger

5 9 2 7 1

Step 1: 5 9 2 7 1
Step 2: 5 9 2 7 1
Step 3: 2 5 9 7 1
Step 4: 2 5 7 9 1
Step 5: 1 2 5 7 9

Time Complexity: O(N*N)
Space Complexity:O(1)

"""

class InsertionSort():

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def sort(self, arr):

        for i in range(len(arr)):
            for j in range(i, 0 , -1):
                if(arr[j] < arr[j-1]):
                    self.swap(arr, j , j-1)

        return arr


print(InsertionSort().sort([2,1,9,5,3]))