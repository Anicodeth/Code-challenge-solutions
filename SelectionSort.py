class Solution: 

    def selectionSort(self, arr,n):
        
        for i in range(n):
            pos=0
            last=n-i-1
            for j in range(last+1):
                if(arr[j]>arr[pos]):
                    pos=j
            arr[pos],arr[last]=arr[last],arr[pos]
