class Solution:
    def isPalindrome(self, s: str) -> bool:
        t= []
        for char in s:
            if char.isalnum():
                t.append(char.lower())
        
        x="".join(t)

        l,r= 0, len(x)-1
        while l<r:
            if x[l]!=x[r]:
                return False
            l+=1
            r-=1
        return True