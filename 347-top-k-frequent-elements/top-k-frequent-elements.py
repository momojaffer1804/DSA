class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num , 0) +1
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1])) #item[1] means frequency , so that when we sort we sort by frequency and not the number itself

        return list(sorted_count.keys())[-k:]
            
        