class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi=max(arr)
        for i in range(len(arr)-1):
            if maxi==arr[i]:
                maxi=max(arr[i+1:])
            arr[i]=maxi
        arr[-1]=-1
        return arr
            
