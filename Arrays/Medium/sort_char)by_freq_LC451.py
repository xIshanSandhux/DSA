class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for x in s:
            if x not in freq:
                freq[x] = 1
            elif x in freq:
                freq[x]+=1
     

        sorted_freq_dec = dict(sorted(freq.items(), key=lambda item: item[1],reverse=True))
       
        result = []
        for char, count in sorted_freq_dec.items():
            result.append(char * count)

        return ''.join(result)

s = Solution()
print(s.frequencySort("tree"))
print(s.frequencySort("cccaaa"))
print(s.frequencySort("Aabb"))