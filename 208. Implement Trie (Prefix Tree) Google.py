class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()     

    def insert(self, word: str) -> None:

        current = self.root

        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                current.children[c] = TrieNode()
                current = current.children[c]

        current.isEnd = True

                
    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                return False

        return current.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for c in prefix:
            if c in current.children:
                current = current.children[c]
            else:
                return False

        return True
        

        
