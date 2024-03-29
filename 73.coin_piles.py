'''
Coin Piles 

There are N piles of coins each containing  Ai (1<=i<=N) coins. Find the minimum number of coins to be removed such that the absolute difference of coins in any two piles is at most K.
Note: You can also remove a pile by removing all the coins of that pile.

https://practice.geeksforgeeks.org/problems/coin-piles5152/1#
'''

// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function Template for C++

class Solution {
  public:
    int minSteps(int arr[], int n, int k)
   {
       sort(arr,arr+n) ;
       
       long long sum = 0 ;
       long long pre[n] = {} ;
       pre[0] = arr[0] ; 
       
       for(int i=1;i<n;i++)
           {
               pre[i] = pre[i-1]+arr[i] ;
           }
           
       sum = pre[n-1] ;
           
       int ans = INT_MAX ;
       
       for(int i=0;i<n;i++)
       {
           int mn = arr[i] ;
           
           int temp = pre[i]-arr[i] ;
           
           int ind = lower_bound(arr+i+1,arr+n,mn+k+1)-arr ;
           
           if(ind<n)
           {
               temp+=(sum-pre[ind]+arr[ind])-(n-ind)*(mn+k) ;
           }
           
           ans = min(ans,temp) ;
       }
       
       return ans ;
   }
};


// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, K;
        cin>>N>>K;
        
        int A[N];
        for(int i=0; i<N; i++)
            cin>>A[i];

        Solution ob;
        cout << ob.minSteps(A,N,K) << endl;
    }
    return 0;
}  // } Driver Code Ends