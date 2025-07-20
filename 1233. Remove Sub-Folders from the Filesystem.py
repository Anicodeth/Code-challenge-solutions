class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, seq):
        temp = self.root

        for c in seq:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.isEnd = True

    def is_sub(self, dirSeq):
        temp = self.root
        
        for c in dirSeq:
            if temp.isEnd:
                return True
            if c not in temp.children:
                return False
            temp = temp.children[c]

        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        trie = Trie()

        for f in folder:
            trie.insert(f.split("/")[1:])

        for f in folder:
            if f not in res and not trie.is_sub(f.split("/")[1:]):
                res.append(f)

        return res
