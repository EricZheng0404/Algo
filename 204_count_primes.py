class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(2, n):
            if isPrime[i]:
                for j in range(2 * i, n, i):
                    isPrime[j] = False

        count = 0
        for i in range(2, n):
            if isPrime[i]: 
                count += 1

        return count
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countPrimes(10))
    