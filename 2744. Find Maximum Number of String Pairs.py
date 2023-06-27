class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
      dic = defaultdict()
      count = 0

      for word in words:
        reverse = word[::-1]
        if reverse in dic:
          count += dic.get(reverse, 0)
          dic[reverse] += 1
        dic[word] = 1

      return count
        
