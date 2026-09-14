class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        # Count the frequency of each element
        count = Counter(nums)
    
        # Create buckets where the index represents the frequency
        # The maximum possible frequency is len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
    
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # Iterate backwards from the highest frequency bucket to collect top k elements
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
