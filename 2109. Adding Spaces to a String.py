class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        newString = []
        spaces = set(spaces)

        for i, c in enumerate(s):
            if i in spaces:
                newString.append(" ")
            newString.append(c)

        return "".join(newString)
