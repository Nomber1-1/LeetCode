class Solution {
    public static int lengthOfLastWord(String s) {
        String[] s1 = s.split(" ");
        return s1[s1.length - 1].length();
    }
    /* 
    public int lengthOfLastWord(String s) {
        s=s.trim();
       
        int j=0;
        for( int i=s.length()-1;i>=0;i--)
        {
            if(s.charAt(i)== ' ') break;
            j++;
        }        
        return j;
    }
    */
    public static void main(String[] args) {
        String s = "Hello World";
        System.out.println(lengthOfLastWord(s));
        System.out.println(s.trim());
    }
}