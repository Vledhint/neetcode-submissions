class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # print(f"puntR: {r}")
            while s[r] in charSet:
                # print(f"Removemos: {s[l]}")
                charSet.remove(s[l])
                # print(f"Sumamos 1 a puntL:: {l}")
                l += 1
                # print(f"Nuevo puntL:: {l}")
            # print(f"Agregamos a charSet: {s[r]}")
            charSet.add(s[r])
            res = max(res, r - l +1)
            # print(f"Nuevo valor de res: {res}")

        return res
        '''rep = set()
        longest = 0
        curr = 0

        if len(s) == 1:
            return 1
        
        for e in s:
            # print(f"Valor a evaluar: {e}")
            if e in rep:
                # print(f"Existe el valor")
                # print(f"Valor maximo a guardar: {longest}, {curr}")
                longest = max(longest, curr)
                rep.clear()
                curr = 1
                rep.add(e)
            else:
                # print(f"No existe el valor; se aumenta contador y se guarda en repetidos")
                curr +=1
                rep.add(e)

            # print(f"Repetidos: {rep}")
            longest = max(longest, curr)

        return longest'''

