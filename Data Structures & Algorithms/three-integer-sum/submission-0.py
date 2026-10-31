class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()

        nums.sort()

        print(f"Numeros ordenados: {nums}")
        
        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums) -1
            while l < r:
                suma = a + nums[l] + nums[r]
                if suma > 0:
                    r -= 1
                elif suma < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        

        '''
        
        for i in range(len(nums)):
            #print(f"Subconjunto: {nums[i+1:]}")
            l, r = i+1, len(nums[i+1:])
            #print(f"NUmero a comparar: {-nums[i]}")
            while l < r:
                if -nums[i] > nums[l] + nums[r]:
                    r -= 1
                elif -nums[i] < (nums[l] + nums[r]):
                    l += 1
                else:
                    result.append([i, l, r])

        
        '''

        return result