class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dicts={}
        ans=[]
        for x in points:
            t=x[0]*x[0]+x[1]*x[1]
            if t in dicts:
                dicts[t].append(x)
            else:
                dicts[t]=[x]
                ans.append(t)
        ans.sort()
        temp=[]
        i=0
        while k>0:
            k-=len(dicts[ans[i]])
            for x in dicts[ans[i]]:
                temp.append(x)
            i+=1
        return temp
