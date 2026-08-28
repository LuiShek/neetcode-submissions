class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        last = s2_len

        if(s1_len<=s2_len):
            left = 0
            right = s1_len - 1
            count1 = Counter(s1)
            while(right<last):
                temp = s2[left:right + 1]
                count2 = Counter(temp)
                if(count1 == count2):
                    return True
                left += 1
                right += 1
        return False
            

        