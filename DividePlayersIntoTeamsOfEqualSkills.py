class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,r=0,len(skill)-1
        target=skill[l]+skill[r]
        prod=0

        while(l<r):
            if(skill[l]+skill[r]==target):
                prod+=(skill[l]*skill[r])
                l+=1
                r-=1
            else:
                return -1

        return prod
