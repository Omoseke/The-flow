class PalindromeChecker:
    @staticmethod
    def is_palindrome(x):
        # Handle special cases
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # For odd-length numbers, reversed_half // 10 removes the middle digit
        return x == reversed_half or x == reversed_half // 10

# Example usage
checker = PalindromeChecker()
print(checker.is_palindrome(121))  # Output: True
print(checker.is_palindrome(-121))  # Output: False
print(checker.is_palindrome(10))    # Output: False
