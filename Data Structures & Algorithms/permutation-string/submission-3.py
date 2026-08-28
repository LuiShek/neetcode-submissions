class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        last = s2_len

        if(s1_len<=s2_len):
            left = 0
            right = s1_len - 1
            while(right<last):
                s1_sort = sorted(s1)
                temp = s2[left:right + 1]
                temp_sort = sorted(temp)
                if(s1_sort == temp_sort):
                    return True
                left += 1
                right += 1
        return False
            

        