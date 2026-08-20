# LeetCode 1518: Water Bottles
#
# Approach:
# - Start with the number of full bottles.
# - Drink all the bottles and get empty bottles.
# - Exchange empty bottles for new full bottles.
# - Drink the new bottles and repeat.
# - Stop when there are not enough empty bottles to exchange.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            new_bottles = empty // numExchange
            total += new_bottles
            empty = empty % numExchange + new_bottles

        return total


# Main
numBottles = int(input("Enter number of bottles: "))
numExchange = int(input("Enter exchange value: "))

obj = Solution()
result = obj.numWaterBottles(numBottles, numExchange)

print("Total bottles drunk:", result)