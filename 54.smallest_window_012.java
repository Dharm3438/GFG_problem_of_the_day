// Smallest window containing 0, 1 and 2 

// Given a string S consisting of the characters 0, 1 and 2. Your task is to find the length of the smallest substring of string S that contains all the three characters 0, 1 and 2. If no such substring exists, then return -1.

// https://practice.geeksforgeeks.org/problems/d6e88f06b273a60ae83992314ac514f71841a27d/1#

// { Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;
import java.lang.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String S = read.readLine();
            Solution ob = new Solution();
            int ans = ob.smallestSubstring(S);

            System.out.println(ans);
        }
    }
}// } Driver Code Ends


// User function Template for Java

class Solution {
    public int smallestSubstring(String S) {
        // Code here
        int j=0,n=S.length();
        int[] mp=new int[3];
        int ans=Integer.MAX_VALUE;
        Arrays.fill(mp,0);
        for(int i=0;i<n;i++){
            mp[S.charAt(i)-'0']++;
            while(mp[S.charAt(j)-'0']>1){
                mp[S.charAt(j++)-'0']--;
            }
            if(mp[0]>0 && mp[1]>0 && mp[2]>0) ans=Math.min(ans,i-j+1);
        }
        return ans==Integer.MAX_VALUE ? -1 : ans;
    }
};
