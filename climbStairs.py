class Solution:
    def climbStairs(self, n: int) -> int:
        ans = {1: 1, 2: 2, 3: 3}

        def f(n):
            if(n not in ans):
                ans[n] = f(n-1) + f(n-2)
            if(n in ans):
                return ans[n]
        return f(n)
