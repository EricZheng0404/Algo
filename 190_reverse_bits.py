class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = bin(n)[2:]
        reversed = binary_str[::-1]
        return int(reversed, 2)