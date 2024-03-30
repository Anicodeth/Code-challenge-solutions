class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def merge(left, right,operator):
            merged = []
            for num1 in left:
                for num2 in right:
                    if operator == '*':
                        merged.append(num1 * num2)
                    elif operator == '+':
                        merged.append(num1 + num2)
                    else:
                        merged.append(num1 - num2)

            return merged

        def recure(express):

            if len(express) == 1 or express.isdigit():
                return [int(express)]

            values = []
            
            for i, c in enumerate(express):

                if c in {'*', '+', '-'}:
                    left = recure(express[:i])
                    right = recure(express[i+1:])
                    merged = merge(left, right, c)

                    values.extend(merged)

            return values


        return recure(expression)

