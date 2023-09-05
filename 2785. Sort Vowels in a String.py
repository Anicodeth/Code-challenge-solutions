class Solution:
    def sortVowels(self, s: str) -> str:
      sliced = list(s)
      vowels = deque()
      
      scope = set(['A','E','I','O','U','a','e','i','o','u'])

      for i,c in enumerate(sliced):
        if  c in scope:
          sliced[i] = '_'
          vowels.append(c)

      vowels = deque(sorted(vowels))
      for i,c in enumerate(sliced):
        if c == '_':
          value = vowels.popleft()
          sliced[i] = value

      return "".join(sliced)

        
