class Solution:
    def recure(self, n):
      if n == '':
        return ''
      elif n[0] == '0':
        return '01' + self.recure(n[1:])
      elif n[0] == '1':
        return '10' + self.recure(n[1:])

    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1: 
            return 0
        half = 2**(N - 2) 
        
        if K > half:
            return 1 if self.kthGrammar(N - 1, K - half) == 0 else 0
        else:
            return self.kthGrammar(N - 1, K)
      
      
      
      
      
      
      
      
      
      # row = '0'
      # for _ in range(n-1):
      #   newrow = ''
      #   for bit in row:
      #     if bit == '0':
      #       newrow += '01'
      #     elif bit == '1':
      #       newrow += '10'
      #   row = newrow
      # return int(row[k-1])

