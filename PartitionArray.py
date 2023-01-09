class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a=[]
        c=0
        for i in nums:
            if i<pivot:
                a.append(i)
            elif i==pivot:
                c+=1
        for i in range(c):
            a.append(pivot)
        for i in nums:
            if i>pivot:
                a.append(i)
        return a
