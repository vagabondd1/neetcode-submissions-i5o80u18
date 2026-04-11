class Solution:
    def topKFrequent(self, nums, k):
        n = len(nums)
        if (n == 1): return nums

        buckets = [ [] for _ in range(n + 1)]
        numbers = Counter(nums)
        answer = []

        for key in numbers:
            buckets[numbers[key]].append(key)
        
        for count in range(len(buckets) - 1, -1, -1):
            for num in buckets[count]:
                answer.append(num)
                if len(answer) == k:
                    return answer
        
        return answer