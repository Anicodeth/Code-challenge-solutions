class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")
        ordered=[""]*len(s)
        res=""
        for i in s:
            ordered[int(i[-1])-1]=i[0:len(i)-1]
        for k in ordered:
            res=res+" "+ k
        return res.strip()
