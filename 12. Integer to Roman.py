class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
            10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
            100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
            1000: 'M'
        }

        if num == 0:
            return ""
        
        result = []
        values = sorted(dic.keys(), reverse=True)

        for value in values:
            while num >= value:
                result.append(dic[value])
                num -= value

        return "".join(result)




        

        
