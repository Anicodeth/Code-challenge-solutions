class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
        

    def search(self, word: str) -> bool:
        return self.search_recursive(word, self.root, 0)

    def search_recursive(self, word: str, node: TrieNode, index) -> bool:
        if not word or index == len(word):
            return node.is_end  

        char = word[index]
        if char != '.':
            if char not in node.children:
                return False  
            return self.search_recursive(word, node.children[char], index + 1)
        else:
            for child_node in node.children.values():
                if self.search_recursive(word, child_node, index + 1):
                    return True
            return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
