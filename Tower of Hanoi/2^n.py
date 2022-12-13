#Time : 2^n
#Space: O(n)
#recurssion
# https://www.codechef.com/problems/HISC05
n = int(input())
def TOH(n,S,Ax,D):
    if n<=0:
        return
    TOH(n-1,S,D,Ax)
    print("Disk ",n,"moved from ",S," to ",D)
    TOH(n-1,Ax,S,D)
TOH(n,"A","B","C")
