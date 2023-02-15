class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r==0 or c==0:
            return []
        reshape=[]   
        merged=[]
        for row in mat:
            merged+=row
        if(c<r):
            r=int(len(merged)/c)
        else:
            c=int(len(merged)/r)
        p=0
        for _ in range(r):
            row=[] 
            temp=c          
            while temp>0:
                row.append(merged[p])
                p+=1
                temp-=1        
            reshape.append(row)
        return reshape
