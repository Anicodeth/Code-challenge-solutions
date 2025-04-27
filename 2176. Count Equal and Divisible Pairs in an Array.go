func countPairs(nums []int, k int) int {
    count := 0
    n := len(nums)

    for i := 0; i < n - 1; i++ {
        for j := i + 1; j < n; j++{
            if nums[i] == nums[j] && (i * j) % k == 0 {
                count ++
            }
        }
    }
    
    return count
}
