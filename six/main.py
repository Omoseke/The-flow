class Solution:
    @staticmethod
    def isPrefixAndSuffix(str1, str2):
        """Check if str1 is both a prefix and suffix of str2."""
        return str2.startswith(str1) and str2.endswith(str1)

    def countPrefixSuffixPairs(self, words):
        """Count the number of index pairs (i, j) such that i < j and str1 is both a prefix and suffix of str2."""
        count = 0
        n = len(words)

        for i in range(n):
            for j in range(i + 1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count

solution = Solution()
words1 = ["a", "aba", "ababa", "aa"]
words2 = ["pa", "papa", "ma", "mama"]
words3 = ["abab", "ab"]

# Testing
print(solution.countPrefixSuffixPairs(words1))  # Output: 4
print(solution.countPrefixSuffixPairs(words2))  # Output: 2
print(solution.countPrefixSuffixPairs(words3))  # Output: 0
