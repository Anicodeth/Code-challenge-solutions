class Solution: 
    def commonChars(self, words: List[str]) -> List[str]:       
        offset = ord('a')
        arrli=[]
        for word in words:
            arrayd = [0]*26
            for char in word:
                ascii = ord(char)
                arrayd[ascii - offset] += 1
            arrli.append(arrayd)
        ma=[]
        for i in range(26):
            max=10000
            for j in arrli:
                if j[i]<max:
                    max=j[i]
            ma.append(max)
        la=[]
        for i in range(len(ma)):
            la.append(chr(i+offset)*ma[i])
        st=("".join(la))
        la=[]
        for c in st:
            la.append(str(c))
        return la
