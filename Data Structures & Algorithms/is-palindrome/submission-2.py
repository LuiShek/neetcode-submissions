class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        for i in range(0, (len(clean))//2): # // return integer
            if(clean[i]!=clean[len(clean)-(i+1)]):
                return False
        return True

        