// Smaller on Left 

// Given an array arr[ ] of N positive integers, the task is to find the greatest element on the left of every element in the array which is strictly smaller than itself, if this element does not exist for an index print "-1".

// https://practice.geeksforgeeks.org/problems/smaller-on-left20360700/1

// { Driver Code Starts
//Initial Template for Java

//Initial Template for Java

//Initial Template for Java

/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;


class Array {
    
    // Driver code
	public static void main (String[] args) throws IOException{
		// Taking input using buffered reader
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int testcases = Integer.parseInt(br.readLine());
		
		// looping through all testcases
		while(testcases-- > 0){
		    int sizeOfArray = Integer.parseInt(br.readLine());
		    int arr [] = new int[sizeOfArray];
		    
		    String line = br.readLine();
		    String[] elements = line.trim().split("\\s+");
		    for(int i = 0;i<sizeOfArray;i++){
		        arr[i] = Integer.parseInt(elements[i]);
		    }
		    
		    Complete obj = new Complete();
		    arr = obj.Smallestonleft(arr, sizeOfArray);
		    for(int i=0; i< sizeOfArray;i++){
		        System.out.print(arr[i] + " ");
		    }
		    System.out.println();
		}
	}
}


// } Driver Code Ends


//User function Template for Java
class Complete{
    public static int[] Smallestonleft (int arr[], int n) {
        int[] ans=new int[n];
        TreeSet<Integer> ts=new TreeSet<>();
        for(int i=0;i<n;i++){
            int k=ts.lower(arr[i])==null? -1:ts.lower(arr[i]);
            ans[i]=k;
            ts.add(arr[i]);
        }
        return ans;
    }
}



