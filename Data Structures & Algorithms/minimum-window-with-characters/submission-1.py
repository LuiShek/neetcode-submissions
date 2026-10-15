class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        left = 0
        satisfied = 0
        required = len(need)
        best_len = float("inf")
        best_start = 0

        for right in range(len(s)):
            ch = s[right]
            have[ch] = have.get(ch, 0) + 1
            if ch in need and have[ch] == need[ch]:
                satisfied += 1

            while satisfied == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                out = s[left]
                have[out] -= 1
                if out in need and have[out] < need[out]:
                    satisfied -= 1
                left += 1

        return "" if best_len == float("inf") else s[best_start : best_start + best_len]