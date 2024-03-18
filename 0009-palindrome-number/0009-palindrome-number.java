class Solution {
    public boolean isPalindrome(int x) {
        // x가 음수이면 팰린드롬 생성 안됨.
        if (x < 0) {
            return false;
        }
        
        // 정수를 문자열로 변환
        String str = String.valueOf(x);
        int left = 0, right = str.length() - 1;
        
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}