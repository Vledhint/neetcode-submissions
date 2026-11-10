class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1) 
        t = [26]

        if len(s1) > len(s2):
            return False

        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        # print(f"Conteo 1: {count1}")
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                # print(f"Conteo 2: {count2}")
                # print(f"Si conteo 1: {count1.get(s2[j], 0)} < {count2[s2[j]]}")
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                # print(f"Si conteo 1: {count1.get(s2[j], 0)} == {count2[s2[j]]}")
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                # print(f"Si actual: {cur} == {need}")
                if cur == need:
                    return True

        return False

