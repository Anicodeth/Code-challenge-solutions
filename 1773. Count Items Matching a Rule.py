class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        count = 0
        dic = {
            "type" : 0,
            "color": 1,
            "name" : 2
        }

        for row in items:
            if row[dic[ruleKey]] == ruleValue:
                count += 1

        return count
