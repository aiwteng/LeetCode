
class Solution {
     public static boolean isPalindrome(int x) {
        String after = "";
        String before = Integer.toString(x);
        Stack<Character> stack = new Stack<>(); //last in first out 

        for(int i=0; i<before.length();i++){
            stack.push(before.charAt(i));
        }

        while(!stack.isEmpty()){
            after+=stack.pop();
        }

        if(after.compareTo(before)==0){
            return true;
        }
        else{
            return false;
        }
    }
}