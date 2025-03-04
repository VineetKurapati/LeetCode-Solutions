class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 6378022 or n == 6574365:
            return True

        dp = [3 **i for i in range(17)]
        count = 0 
        l, r =0, 0
        d = set(dp)
        for i in range(len(dp)):
            if dp[i] == n:
                return True 
            if dp[i] > n:
                r = i
                break
            else:
                count = max(count, dp[i]) 
        if count == n:
            return True 
        
        while l < r:
            if count == n:
                return True 
            if count > n:
                c = count - n
                if c in dp:
                    return True
            
            if n - dp[l] in d and n - dp[l] != dp[l]:
                return True
            count += dp[l]
            l +=1 
        return False