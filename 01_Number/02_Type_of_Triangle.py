# LeetCode 3024: Type of Triangle
#
# Approach:
# Sort the three sides and first check whether they
# can form a valid triangle.
#
# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def triangleType(self, nums):
        nums.sort()

        a, b, c = nums

        # Triangle inequality
        if a + b <= c:
            return "none"

        # All three sides are equal
        if a == b == c:
            return "equilateral"

        # Any two sides are equal
        if a == b or b == c:
            return "isosceles"

        # All sides are different
        return "scalene"
nums = list(map(int, input("Enter three sides: ").split()))
obj=Solution()
print(obj.triangleType(nums))
