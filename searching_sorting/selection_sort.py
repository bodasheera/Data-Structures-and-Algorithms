""" SELECTION SORT

Selection sort is a sorting algorithm that selects the smallest element from an unsorted list
in each iteration and places that element at the beginning of the unsorted list.

1.loop through array 
2. find smallest element from i to N-1 
3. if small is less than current element swap it

Time complexity: O(N*N)
Space Complexity: O(1)
"""



class SelectionSort():

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def sort(self, arr):
        for i in range(len(arr)-1):
            small = i
            for j in range(i, len(arr)):

                if (arr[j]<arr[small]):
                    small = j

            if (arr[small] < arr[i]):    
                self.swap(arr, small , i)

        print(arr)


SelectionSort().sort([9,2,5,1,7])