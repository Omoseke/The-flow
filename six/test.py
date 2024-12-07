class Solution:
    @staticmethod
    def longest_common_prefix(strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Compare the prefix with each string
        for s in strs[1:]:
            while not s.startswith(prefix):
                # Reduce the prefix
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

# Example usage
solution = Solution()
print(solution.longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(solution.longest_common_prefix(["dog", "racecar", "car"]))     # Output: ""
