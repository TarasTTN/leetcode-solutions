import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1
        res = []

        for i in range(n - 1, -1, -1):
            fact = math.factorial(i)
            idx = k // fact
            res.append(numbers.pop(idx))
            k %= fact

        return "".join(res)