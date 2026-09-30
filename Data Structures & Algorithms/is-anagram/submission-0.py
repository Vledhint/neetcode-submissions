class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns = sorted(s)
        nt = sorted(t)

        if ns == nt:
            return True

        return False