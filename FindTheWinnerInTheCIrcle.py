class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[]
        p=0
        for i in range(1,n+1):
            arr.append(i)
        
        while(len(arr)!=1):         
            size=len(arr)
            arr.pop((p+k-1)%size)
            p=(p+k-1)%size
        return arr[0]

            
