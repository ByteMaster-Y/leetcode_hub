class Solution {
    public int mySqrt(int x) {
        if(x == 0 || x == 1) {
            return x;
        }
        
        // 제곱근이 될 수 있는 범위의 왼쪽 끝
        long left  = 0;
        long right = x;
        
        while (left <= right) {
            long mid = left + (right - left) / 2;
            
            if (mid * mid == x) {
                return (int)mid;
            } else if (mid * mid < x) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        // 이진 탐색 후에도 제곱근을 찾지 못한 경우, right 값이 제곱근이 됨
        return (int)right;
    }
}