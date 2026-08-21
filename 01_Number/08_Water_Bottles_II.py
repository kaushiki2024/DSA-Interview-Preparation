# LeetCode 3100: Water Bottles II
#
# Approach:
# - Start with the number of full bottles.
# - Drink all the bottles and get empty bottles.
# - Exchange empty bottles for new full bottles.
# - After every exchange, the exchange value increases by 1.
# - Drink the new bottle and get 1 empty bottle.
# - Stop when there are not enough empty bottles to exchange.
#
# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            empty = empty - numExchange
            total += 1
            empty += 1
            numExchange += 1

        return total


# Main
numBottles = int(input("Enter number of bottles: "))
numExchange = int(input("Enter exchange value: "))

obj = Solution()
result = obj.maxBottlesDrunk(numBottles, numExchange)

print("Total bottles drunk:", result)