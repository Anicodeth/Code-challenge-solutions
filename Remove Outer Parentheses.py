class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        valid_expression = []
        opened_count = 0

        for char in S:
            if char == '(' and opened_count > 0:
                valid_expression.append(char)
            if char == ')' and opened_count > 1:
                valid_expression.append(char)
            opened_count += 1 if char == '(' else -1

        return "".join(valid_expression)
