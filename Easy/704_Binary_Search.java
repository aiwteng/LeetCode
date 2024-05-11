class Solution {
    public int search(int[] nums, int target) {
        int head = 0;
        int tail = nums.length-1;
        
        while(head<=tail){
            int middle = (tail + head)/2;
            if(nums[middle] < target){
                head = middle + 1;
            } else if(nums[middle] > target){
                tail = middle - 1;
            }else{
                return middle;
            }
        }
        return -1;
    }
}
