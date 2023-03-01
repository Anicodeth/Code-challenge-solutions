class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
      que = deque(tickets)
      count = 0

      while(que[k] != 0):
        for i in range(len(tickets)):
          if que[k-i] == 0:
            return count
          front = que.popleft()
          if front != 0:
            que.append(front-1)
            count+=1
          else:
            que.append(front)
      return count
