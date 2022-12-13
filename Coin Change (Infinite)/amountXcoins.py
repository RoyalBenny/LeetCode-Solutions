#Time: O(coins*amount)
#Space: O(amount)
#Dynamic Programming
#https://leetcode.com/problems/coin-change-2/
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        total = [0]*(amount+1)
        total[0] = 1
        for c in coins:
            for j in range(c,amount+1):
                total[j]+= total[j-c]
        return total[-1]
