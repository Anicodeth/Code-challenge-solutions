class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        possible = []

        for word in dictionary:
            p1 = 0
            valid = False
            n = len(word)
            for c in s:
                if p1 == n:
                    valid = True
                    break
                if c == word[p1]:
                    p1 += 1
            if p1 == n:
                valid = True

            if valid: possible.append(word)


        if not possible: return ""

        possible.sort(key = lambda x : (len(x), x))

        wanted = len(possible[-1])

        for word in possible:
            if len(word) == wanted:
                return word
