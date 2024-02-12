class Solution {
    public int strStr(String haystack, String needle) {
        int size_n = needle.length();
        int size_h = haystack.length();
        String temp = "";
        
        if (!haystack.contains(needle)) {
            return -1;
        }

        int i = 0;
        while (i < size_h - size_n + 1) {
            if (haystack.charAt(i) == needle.charAt(0)) {
                temp = "";
                for (int j = 0; j < size_n; j++) {
                    temp += haystack.charAt(i+j);
                }
                System.out.print(temp);
                if (temp.equals(needle)) {
                    return i;
                }
            }
            i += 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        haystack = "sadbutsad";
        needle = "sad";
        System.out.print(strStr(haystack, needle));
    }
}