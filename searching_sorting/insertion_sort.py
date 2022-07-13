"""INSERTION SORT

Intuition
Like sorting a pack of cards
You will be inserting a element in sorted array 
at every pass arr[0, i-1] will be already sorted


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