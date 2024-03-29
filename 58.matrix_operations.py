'''
Matrix Operations 

Given a binary matrix of dimensions N * M. One can perform the given operation in the matrix.

If the value of matrix[i][j] is 0, then traverse in the same direction and check the next value.
If the value of matrix[i][j] is 1, then update matrix[i][j] to 0 and change the current direction from up, right, down, or left to the directions right, down, left, and up respectively.
Initially you start from cell(0, 0), moving in right direction.

The task is to find the indices of the matrix  which leads to outside the matrix from the traversal of the given matrix from the cell (0, 0) by performing the operations.

https://practice.geeksforgeeks.org/problems/7d7f73a59ddc3f9c8046af6bd66ea67311bf877e/1#
'''

#User function Template for python3

class Solution:
    def endPoints(self, matrix, m, n):
        def get(x,y,d):
            if(d=='R'):
                return (x,y+1)
            elif(d=='L'):
                return (x,y-1)
            elif(d=='U'):
                return (x-1,y)
            else:
                return (x+1,y)
        
        def solve(x,y,d):
            if(matrix[x][y]==0):
                nx,ny = get(x,y,d)
                nd=d
            else:
                matrix[x][y]=0
                if d=='U':
                    nx,ny = get(x,y,'R')
                    nd = 'R'
                elif d=='R':
                    nx,ny = get(x,y,'D')
                    nd = 'D'
                elif d=='D':
                    nx,ny = get(x,y,'L')
                    nd = 'L'
                elif d=='L':
                    nx,ny = get(x,y,'U')
                    nd = 'U'
            
            if 0<=nx<len(matrix) and 0<=ny<len(matrix[0]):
                return solve(nx,ny,nd)
            else:
                return (x,y)
        
        return solve(0,0,'R')

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix,r,c)
        print('(',ans[0],', ',ans[1],')',sep ='')

# } Driver Code Ends