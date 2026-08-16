# LeetCode 258: Add Digits
#
# Approach:
# find sum of digits
# if sum is not a single digit, call the same function again
# repeat until single digit is obtained
#
# Time Complexity: O(log n)
# Space Complexity: O(log n) due to recursion

class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0

        while num > 0:
            digit = num % 10
            sum += digit
            num //= 10

        if sum >= 0 and sum <= 9:
            return sum
        else:
            return self.addDigits(sum)


# Main
num = 38

obj = Solution()
print(obj.addDigits(num))