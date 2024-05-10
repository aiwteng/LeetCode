class Solution {
    public static int longestConsecutive(int[] nums) {
        //initialise set
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num); //add all number into set, bcs set can use .contain()
        }

        int longest = 0; //act as counter

        for (int n : nums) { //loop through all number in array
            if (!numSet.contains(n - 1)) { //for eg: no.1, 1-1=0, there is no 0 in the array, execute following
                int length = 0; 
                while (numSet.contains(n + length)) { //1+1, there is 2 in the array, length counter +1
                    length++;
                }
                longest = Math.max(length, longest); //compare, find the largest one
            }
        }
        return longest;
    }
}
