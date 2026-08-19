# LeetCode 1342: Number of Steps to Reduce a Number to Zero
#
# Approach:
# - If the number is even, divide it by 2.
# - If the number is odd, subtract 1 from it.
# - Repeat these steps until the number becomes 0.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0

        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1

            step += 1

        return step


# Main
if __name__ == "__main__":
    num = int(input("Enter a number: "))

    obj = Solution()
    result = obj.numberOfSteps(num)

    print("Number of steps:", result)