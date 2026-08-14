# LeetCode 3783: Mirror Distance of an Integer
#
# Approach:
# 1. Find the reverse of the number.
# 2. Calculate the absolute difference between the number and its reverse.
#
# Time Complexity: O(d), where d is the number of digits in n.
# Space Complexity: O(1)

# LeetCode 3783: Mirror Distance of an Integer
#
# Approach:
# 1. Find the reverse of the number.
# 2. Calculate the absolute difference between the number and its reverse.
#
# Time Complexity: O(d), where d is the number of digits in n.
# Space Complexity: O(1)


class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        x = n

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        return abs(n - rev)


def main():
    print(Solution().mirrorDistance(123))


main()