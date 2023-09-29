class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False 
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        res = []
        words = set(wordDict)
        n = len(s)

        def backtrack(start, sentence):
            if start == n:
                res.append(" ".join(sentence))
                return

            for end in range(start, n):
                word = s[start:end + 1]
                if word in words:
                    sentence.append(word)
                    backtrack(end + 1, sentence)
                    sentence.pop()

        backtrack(0, [])


        return res

