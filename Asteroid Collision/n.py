#Time : O(N)
#Space : O(N)
#stack
#https://leetcode.com/problems/asteroid-collision/
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                stack.append((asteroids[i],i))
                continue
            
            while stack:
                if stack[-1][0] == abs(asteroids[i]):
                    asteroids[stack[-1][1]] = 0
                    asteroids[i] = 0
                    stack.pop(-1)
                elif stack[-1][0]> abs(asteroids[i]):
                    asteroids[i] = 0
                    break
                else:
                    asteroids[stack[-1][1]] = 0
                    stack.pop(-1)
        return list(filter(lambda x: x!=0,asteroids))
