class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fiz=[]
        for j in range(1,n+1):
            if j%3==0 and j%5==0:
                fiz.append("FizzBuzz")
            elif j%3==0:
                fiz.append("Fizz")
            elif j%5==0:
                fiz.append("Buzz")
            else:
                fiz.append(f"{j}")

        return fiz
