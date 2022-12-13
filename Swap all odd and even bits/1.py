#User function Template for python3
#Time : O(1)
#Spcae: O(1)
# bit
#https://practice.geeksforgeeks.org/problems/swap-all-odd-and-even-bits-1587115621/1/#

class Solution:
    
    ##Complete this function
    #Function to swap odd and even bits.
    def swapBits(self,n):
        #Your code here
        return ((n & 0xaaaaaaaa) >> 1) | (n & 0x55555555)<<1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.swapBits(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
