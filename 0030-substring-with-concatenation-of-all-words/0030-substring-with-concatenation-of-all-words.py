from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        n = len(s)

        if n < total_len:
            return []

        word_count = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            current_count = Counter()
            words_used = 0

            for right in range(offset, n - word_len + 1, word_len):
                word = s[right : right + word_len]

                if word in word_count:
                    current_count[word] += 1
                    words_used += 1

                    while current_count[word] > word_count[word]:
                        left_word = s[left : left + word_len]
                        current_count[left_word] -= 1
                        words_used -= 1
                        left += word_len

                    if words_used == num_words:
                        result.append(left)
                        left_word = s[left : left + word_len]
                        current_count[left_word] -= 1
                        words_used -= 1
                        left += word_len
                else:
                    current_count.clear()
                    words_used = 0
                    left = right + word_len

        return result