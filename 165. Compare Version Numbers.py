class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        if len(v1) > len(v2):
            v2.extend([ "0" for _ in range(len(v1) - len(v2))])
        else:
            v1.extend([ "0" for _ in range(len(v2) - len(v1))])
        for a, b in zip(v1, v2):
            if int(a) > int(b):
                return 1
            elif int(a) < int(b):
                return -1

        return 0
        
