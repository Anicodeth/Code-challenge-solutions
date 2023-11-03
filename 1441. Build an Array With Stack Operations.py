class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        size = len(target)
        j = 1
        ops = []

        for i in range(size):
            if target[i] == j:
                ops.append("Push")
                j += 1
            else:
                remove = 0
                while target[i] != j:
                    remove += 1
                    j += 1
                for _ in range(remove):
                    ops.append("Push")
                for _ in range(remove):
                    ops.append("Pop")
                ops.append("Push")
                j += 1
                

        return ops
        
