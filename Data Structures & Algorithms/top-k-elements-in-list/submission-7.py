class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rep = dict()
        nums.sort()

        for n in nums:
            if n in rep:
                rep[n] = rep[n] + 1
            else:
                rep[n] = 1
            
        # print(f"Diccionario de repetidos: {rep}")
        desc = {k:v for k, v in sorted(rep.items(), key=lambda item: item[1], reverse=True)}
        # print(f"Diccionario de repetidos ordenado: {desc}")
        repList = list(desc)

        # print(f"Repetidos: {repList}")

        return repList[:k]

