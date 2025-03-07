class Solution:
    def _sieve(self, upperlimit):
        sieve = [True] * (upperlimit + 1)
        sieve[0] = False
        sieve[1] = False 
        for i in range(upperlimit + 1):
            if sieve[i]:
                for n in range(i * i, upperlimit + 1, i):
                    sieve[n] = False 
        return sieve
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = self._sieve(right)
        primes = [num for num in range(left, right + 1) if sieve[num]]
        if len(primes) < 2:
            return (-1, -1)
        min_diff = float("inf")
        res = (-1, -1)
        for i in range(1, len(primes)):
            curr_diff = primes[i] - primes[i-1]
            if curr_diff < min_diff:
                res = (primes[i-1], primes[i])
                min_diff = curr_diff
        return res