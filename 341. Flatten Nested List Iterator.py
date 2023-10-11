class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        for item in reversed(nestedList):
            self.stack.append(item)

    def hasNext(self):
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            nested_list = self.stack.pop()
            for item in reversed(nested_list.getList()):
                self.stack.append(item)
        return False

    def next(self):
        if self.hasNext():
            return self.stack.pop().getInteger()
