class Solution:
    def topKFrequent(self, nums, k):
        n = len(nums)
        if (n == 1): return nums

        buckets = [ [] for _ in range(n + 1)]
        numbers = Counter(nums)
        answer = []

        for key in numbers:
            buckets[numbers[key]].append(key)
        
        while (k > 0 and n >= 0):
            if (buckets[n] != []):
                for num in buckets[n]:
                    answer.append(num)
                    k -= 1
            n -= 1
        
        return answer