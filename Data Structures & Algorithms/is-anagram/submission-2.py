class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        ns = sorted(s)
        nt = sorted(t)

        if ns == nt:
            return True

        return False