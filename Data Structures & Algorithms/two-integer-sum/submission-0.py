class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap
        indices = {}

        for i, n in enumerate(nums):
            # Guardas los numeros con sus indices
            indices[n] = i

        print(indices)

        for i, n in enumerate(nums):
            # Obtienes la diferencia entre el numero y el target
            diff = target - n
            # A la diferencia la buscas en los indices
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        return []