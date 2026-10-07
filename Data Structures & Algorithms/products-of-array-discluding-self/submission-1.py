class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

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

