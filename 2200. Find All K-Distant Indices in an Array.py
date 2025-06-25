class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        n = len(nums)
        k_distant_indices = []

        key_indices = []
        for j in range(n):
            if nums[j] == key:
                key_indices.append(j)

        for i in range(n):
            for j_key in key_indices:
                if abs(i - j_key) <= k:
                    k_distant_indices.append(i)
                    break 

        return k_distant_indices
