'''
Exactly one swap 

Given a string S containing lowercase english alphabet characters. The task is to calculate the number of distinct strings that can be obtained after performing exactly one swap.
In one swap,Geek can pick two distinct index i and j (i.e 1 < i < j < |S| ) of the string, then swap the characters at the position i and j.

https://practice.geeksforgeeks.org/problems/2ac2f925b836b0625d848a0539ffd3d2d2995f92/1#
'''

#User function Template for python3
class Solution:
    def countStrings(self, S): 
        n = len(S)
        charSet = {}
        count = 0
        for i in S:
            if i in charSet:
                count = count + charSet[i] + 1
                charSet[i] += 1
            else:
                charSet[i] = 0
        ans = (n*(n-1)) // 2
        if(count >0):
            ans = ans - count + 1
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countStrings(S)
        print(ans)
# } Driver Code Ends