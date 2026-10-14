class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        clean = ''.join(ch for ch in s_lower if ch.isalnum())

        clean_r = clean[::-1]

        #print(f"Cadena limpia: {clean}")
        #print(f"Cadena reverse: {clean_r}")
        if clean == clean_r:
            return True

        return False