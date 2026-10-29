class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
        
        '''
        result = {}
        
        for n in range(len(numbers)):
            res = target - numbers[n]
            if res in numbers and numbers[n] != res:
                result.add(n+1)
                result.add(numbers.index(res) + 1)

        return list(result)
        '''
            