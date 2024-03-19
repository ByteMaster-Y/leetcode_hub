class Solution {
    public String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();
        int carry = 0;
        // 두 이진수의 길이를 맞추기 위해 짧은 이진수에 앞에 0을 추가
        int maxLength = Math.max(a.length(), b.length());
        a = String.format("%" + maxLength + "s", a).replace(' ', '0');
        b = String.format("%" + maxLength + "s", b).replace(' ', '0');
        
        // 오른쪽에서부터 왼쪽으로 덧셈 수행
        for (int i = maxLength - 1; i >= 0; i--) {
            int digitSum = Character.getNumericValue(a.charAt(i)) + Character.getNumericValue(b.charAt(i)) + carry;
            
            // 이 때 % 2를 사용하여 이진수로 변환한 값을 얻습니다. 
            // 예를 들어, 현재 자리의 합이 0이거나 1이라면 그대로 추가되지만, 
            // 2일 경우 0이 추가되고 carry가 발생합니다.
            result.insert(0, digitSum % 2);
            carry = digitSum / 2;
        }
        
        // 마지막 carry가 남아있으면 결과에 추가
        if (carry > 0) {
            result.insert(0, '1');
        }
        
        return result.toString();
    }
}
