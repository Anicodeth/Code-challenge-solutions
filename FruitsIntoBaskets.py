class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_types = Counter()
        distinct = 0
        max_fruits = 0
        
        left = right = 0
        while right < len(fruits):

            if fruit_types[fruits[right]] == 0:
                distinct += 1
            fruit_types[fruits[right]] += 1
            

            while distinct > 2:
                fruit_types[fruits[left]] -= 1
                if fruit_types[fruits[left]] == 0:
                    distinct -= 1
                left += 1
            
  
            max_fruits = max(max_fruits, right-left+1)
            right += 1
        
        return max_fruits
