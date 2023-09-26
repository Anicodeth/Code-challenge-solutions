class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.value += delta

    def sum(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.value
