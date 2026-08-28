class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)<=len(s2)):
            left = 0
            right = len(s1) - 1
            while(right<len(s2)):
                temp = s2[left:right + 1]
                temp_sort = sorted(temp)
                if(sorted(s1) == temp_sort):
                    return True
                left += 1
                right += 1
        return False
            

        