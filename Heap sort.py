
import heapq 

class Solution:

    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        heapq.heapify(arr)
        for _ in range(n):
            print( heapq.heappop(arr) , end= ' ')
        
