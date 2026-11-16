class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"

        for _ in range(n - 1):
            next_parts = []
            i = 0
            length = len(current)

            while i < length:
                count = 1
                while i + 1 < length and current[i] == current[i + 1]:
                    i += 1
                    count += 1

                next_parts.append(str(count))
                next_parts.append(current[i])
                i += 1

            current = "".join(next_parts)

        return current