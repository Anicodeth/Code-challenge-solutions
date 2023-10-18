class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        
        def count_overlap(x_offset, y_offset):
            count = 0
            for i in range(n):
                for j in range(n):
                    if (i + x_offset >= 0 and i + x_offset < n and
                        j + y_offset >= 0 and j + y_offset < n):
                        count += img1[i][j] & img2[i + x_offset][j + y_offset]
            return count
        
        max_overlap = 0
        for x_offset in range(-n + 1, n):
            for y_offset in range(-n + 1, n):
                max_overlap = max(max_overlap, count_overlap(x_offset, y_offset))
        
        return max_overlap
