class Solution:
    def countTime(self, time: str) -> int:
        maxTime = (23 * 60) + 59
        answer = 0
        n = 4

        def checkTime(time):
            totalTime = (int(time[0] + time[1]) * 60) + (int(time[2] + time[3]))
            if maxTime >= totalTime and int(time[0] + time[1]) < 25 and int(time[2] + time[3]) < 60 :
                return True


        def recure(time, index):
            nonlocal answer
            if index == n:
                if checkTime(time):
                    print(time)
                    answer += 1
                return

            if time[index] != '?':
                recure(time, index + 1)
            else:
                for i in range(10):
                    time[index] = str(i)
                    recure(time, index + 1)
                    time[index] ='?'


        recure([c for c in time if c != ':'], 0)


        return answer
