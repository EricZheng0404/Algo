"""
Leetcode 204: Count Primes

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4

Time complexity: O(n log log n)
Space complexity: O(n)
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        # We set up a list to store if the number is prime
        isPrime = [True] * n
        # We start from 2 because 0 and 1 are not prime numbers, and we don't need to check the number itself
        # We only need to check up to the square root of n because if n is divisible by some number p, then n = p * q and if p <= q then p * p <= n
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                # We start from 2 * i because we don't need to check the number itself
                for j in range(2 * i, n, i):
                    isPrime[j] = False
        # We count the number of prime numbers
        count = 0
        for i in range(2, n):
            if isPrime[i]: 
                count += 1

        return count
    

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countPrimes(10))
    