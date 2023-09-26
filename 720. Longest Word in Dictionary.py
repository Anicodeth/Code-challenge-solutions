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
        for i, c in enumerate(word):
            if c not in node.children or (not node.is_end and i != 0):
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
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = ""
        for word in words:
            if trie.search(word):
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word 
      
        
        return res

