class Solution {
    public boolean isPalindrome(String s) {
        if (s.isEmpty()) {
            return true;
        }

        int start = 0;
        int last = s.length() - 1;

        while (start < last) {
            char head = s.charAt(start);
            char tail = s.charAt(last);

            if (!Character.isLetterOrDigit(head)) {
                start++;
            } else if (!Character.isLetterOrDigit(tail)) {
                last--;
            } else {
                if (Character.toLowerCase(head) != Character.toLowerCase(tail)) {
                    return false;
                }
                start++;
                last--;
            }
        }
        return true;
    }
}
