class Solution:
    def simplifyPath(self, path: str) -> str:
      
      stack = []
      items = path.split('/')
      for s in items:
        if s != '.' and s !='..' and s != '':
          stack.append(s)
        elif s == '..':
          if stack:
            stack.pop()
      new_path = "/" if stack else "//"

      for s in stack:
        new_path+=s+'/'

      return new_path[:len(new_path)-1]




      
          
