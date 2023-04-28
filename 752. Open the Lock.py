class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

      dead = set(deadends)

      q = deque([('0000', 0)])
 
      seen = set('0000')

      while q:
          state, moves = q.popleft()
          if state == target:
              return moves
          if state in dead:
              continue

          for i in range(4):
              for d in (-1, 1):
                  new_digit = (int(state[i]) + d) % 10
                  new_state = state[:i] + str(new_digit) + state[i+1:]
                  if new_state not in seen:
                      seen.add(new_state)
                      q.append((new_state, moves+1))

      return -1
