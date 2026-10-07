class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        output = [0] * size
        pref = [0] * size
        suff = [0] * size

        pref[0] = suff[size - 1] = 1
        for i in range(1, size):
            pref[i] = nums[i -1] * pref[i -1]
        for i in range(size - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(size):
            output[i] = pref[i] * suff[i]

        return output

        """
        for n in range(0, size):
            print(f"Valor a evitar: {n}")
            prefix, suffix = [], []
            for idx, i in enumerate(nums):
                if idx != n:
                    prefix.append(i)
            for j in range((size-1), -1, -1):
                print(f"Valor de j: {j}")
                if j != n:
                    suffix.append(nums[j])
            print(f"Valor de prefix: {prefix}")
            print(f"Valor de suffix: {suffix}")
            output[n] = prefix[n]*suffix[n]
            """

