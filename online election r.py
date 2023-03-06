class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leading =[]
    
        self.times = []
        
        count = defaultdict(int)
        ma = 0
        
        for i , p in enumerate(persons):
            
            count[p]+=1
            
            if count[p]>= ma:
                
                ma= count[p]
                self.leading.append(p)
                self.times.append(times[i])
            
            
    def search(self, ar , target):
        l,r = 0,len(ar)-1
        while l<=r:
                
            mid = l+(r-l)//2
            if ar[mid] == target:
                return mid
            elif ar[mid] > target:
                r = mid-1
            else:
                l= mid+1
        return l-1
        
        

    def q(self, t: int) -> int:
        
        index = self.search(self.times, t)
        return self.leading[index]
        
