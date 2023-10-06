class SnapshotArray:
    def __init__(self, length):
        self.data = [[(0, 0)] for _ in range(length)]  
        self.snap_id = 0

    def set(self, index, val):
        self.data[index].append((self.snap_id, val))

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        snapshots = self.data[index]
        l, r = 0, len(snapshots) - 1
        res = 0
        
        while l <= r:
            m = (l + r) // 2
            
            if snap_id >= snapshots[m][0]:
                res = m
                l = m + 1
            else:
                r = m - 1

        return snapshots[res][1]
