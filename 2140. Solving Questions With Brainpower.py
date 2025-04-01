class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
       
        @cache       
        def dp(index):
            nonlocal n
            if index >= n:
                return 0      
            elif index == n - 1:
                return questions[index][0]  

            #picking 
            pick = questions[index][0] + dp(index + questions[index][1] + 1)

            #not picking
            noPick = dp(index + 1)

            return max(pick, noPick)

        return dp(0)
