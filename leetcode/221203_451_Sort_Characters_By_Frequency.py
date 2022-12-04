class Solution:
    def frequencySort(self, s: str) -> str:
        s_count = Counter(s)
        s_sort = sorted(s_count.items(), key=lambda x: x[0])
        s_sort = sorted(s_count.items(), key=lambda x: x[1], reverse=True)   
        
        
        ans = []
        for k, v in s_sort:
            print(k, v)
            for _ in range(v):
                ans.append(k)
        return ans