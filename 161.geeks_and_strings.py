class Solution:
    #Function to remove pair of duplicates from given string using Stack.
    def removePair(self,s):
        # code here
        stack=['']
        for i in s:
            if stack[-1]==i:
                stack.pop()
                continue
            else:
                stack.append(i)
        if len(stack)>1:
            return ''.join(stack)
        else:
            return -1
