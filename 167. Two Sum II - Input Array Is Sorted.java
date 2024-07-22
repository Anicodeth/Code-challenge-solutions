class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length - 1;
        int [] res = {-1, -1};
        while( l <= r ){
            int sumi = numbers[l] + numbers[r];

            if (sumi > target){
                r -= 1;
            }else if (sumi < target){
                l += 1;
            }
            else {
                res[0] = l + 1;
                res[1] = r + 1;
                return res;
            }
        }
        return res;
        
    }
}
