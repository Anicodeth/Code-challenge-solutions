class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
   

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

        

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        words = sentence.split(" ")

        for i, word in enumerate(words):
            for j in range(1, len(word)):
                if trie.search(word[:j]):
                    words[i] = word[:j]
                    break

        return " ".join(words)

