class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length())
            return false;
        
        int[] arr = new int[26];

        for(int i = 0; i < s.length(); i++) {
           arr[getIntValue(s.charAt(i))] += 1;
           arr[getIntValue(t.charAt(i))] -= 1;
            
        }
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] != 0)
                return false;
        }
        return true; 
    }

    private int getIntValue(char ch) {
        int intValue = ch - 'a';
        return intValue;
    }
}
