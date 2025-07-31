def monotonic(nums):
        n = len(nums)
        res = [0] * n
        s = [] 
        for i in range(n - 1, -1, -1):
            num = nums[i]
            # We get rid of all the number that's less than the num
            while s and s[-1] <= num:
                s.pop()
            res[i] = -1 if not s else s[-1]
            s.append(num)
        return res

print(monotonic([2, 1, 2, 4, 3]))    