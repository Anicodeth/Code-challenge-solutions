class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

      dic = {}

      for i,s in enumerate(list1):
        dic[s] = i

      mini = inf
      res = ""

      for i,s in enumerate(list2):
        if s in dic:
          local = i + dic[s]
          if local < mini:
            mini = local
            res = [s]
          elif mini == local:
            res.append(s)



      return res
