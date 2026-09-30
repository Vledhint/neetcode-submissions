class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        duplicates = []

        for n in nums:
            if n in seen:
                duplicates.append(n)
            else:
                seen.add(n)

        if len(duplicates)>0:
            return True
            
        return False
                