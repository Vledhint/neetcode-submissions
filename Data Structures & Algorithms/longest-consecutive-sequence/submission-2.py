class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        largest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                largest = max(length, largest)
        return largest
        '''
        nums = []
        largest = 0
        nums.sort()
        
        for n in nums:
            if len(cons_seen) == 0:
                cons_seen.append(n)
                continue
            
            if n in cons_seen:
                continue
            
            if n - cons_seen[-1] == 1:
                cons_seen.append(n)
            
            # print(f"Secuencia vista: {cons_seen}")
        
        return len(cons_seen)
        '''
                
