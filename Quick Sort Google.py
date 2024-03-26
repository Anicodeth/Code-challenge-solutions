def quick_sort(nums, left, right):
    if left >= right:
        return
    
    pivot = partition(nums, left, right)
    
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)

def partition(nums, left, right) -> int:
    
    pivot = nums[left]
    store = left + 1
    
    for runner in range(store, right + 1):
        if nums[runner] < pivot:
            nums[runner], nums[store] = nums[store], nums[runner]
            store += 1
            
    nums[store - 1], nums[left] = nums[left], nums[store - 1]
    
    return store - 1
            
