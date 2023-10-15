class Solution:
    def frequencySort(self, s):
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    
        sorted_chars = sorted(freq, key=freq.get, reverse=True)

        sorted_str = ""
        for char in sorted_chars:
            sorted_str += char * freq[char]
    
        return sorted_str

# Input
s = input("Enter a string: ")

# Output
solution = Solution()
result = solution.frequencySort(s)
print("Sorted string by character frequency:", result)
