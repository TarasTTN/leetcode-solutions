class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res, line, length = [], [], 0
        for w in words:
            if length + len(line) + len(w) > maxWidth:
                for i in range(maxWidth - length):
                    line[i % (len(line) - 1 or 1)] += ' '
                res.append(''.join(line))
                line, length = [], 0
            line.append(w)
            length += len(w)
        res.append(' '.join(line).ljust(maxWidth))
        return res
        