class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        best = 0

        for right in range(len(s)):
            char = s[right]
            if char in count:
                count[char] = count[char] + 1
            else:
                count[char] = 1

            while (right - left + 1) - max(count.values()) > k:
                left_char = s[left]
                count[left_char] = count[left_char] - 1
                left += 1

            best = max(best, right - left + 1)

        return best