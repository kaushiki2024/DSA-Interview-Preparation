# LeetCode 3536: Maximum Product of Two Digits
#
# Approach:
# Store all digits in a list.
# Sort the digits in descending order.
# Multiply the two largest digits.
#
# Time Complexity: O(d log d)
# Space Complexity: O(d)

class Solution:
    def maxProduct(self, n: int) -> int:
        digit = []

        while n > 0:
            digit.append(n % 10)
            n //= 10

        digit.sort(reverse=True)

        return digit[0] * digit[1]


# Main
n = 1234

obj = Solution()
print(obj.maxProduct(n))