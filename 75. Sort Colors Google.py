class Solution:
    def sortColors(self, nums: List[int]) -> None:

        def mergeSort(arr, l, r):
            if l == r:
                return [arr[l]]

            m = (l + r) // 2
            
            left = mergeSort(arr, l, m)
            right = mergeSort(arr, m + 1, r)

            return merge(left, right)
            

        def merge(left, right):
            merged = []
            
            p1 = p2 = 0

            n, m= len(left),len(right)

            while p1 < n and p2 < m:

                if left[p1] >= right[p2]:
                    merged.append(right[p2])
                    p2 += 1

                else:
                    merged.append(left[p1])
                    p1 += 1

            if p1 < n:
                for j in range(p1, n):
                    merged.append(left[j])
            
            if p2 < m:
                for j in range(p2, m):
                    merged.append(right[j])


            return merged

        sortedArr = mergeSort(nums, 0, len(nums) - 1)

        for i, num in enumerate(sortedArr):
            nums[i] = num
