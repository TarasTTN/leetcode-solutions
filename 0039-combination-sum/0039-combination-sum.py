class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def backtrack(start_idx: int, path: list[int], remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start_idx, len(candidates)):
                num = candidates[i]
                if num > remaining:
                    break

                path.append(num)
                backtrack(i, path, remaining - num)
                path.pop()

        backtrack(0, [], target)
        return result