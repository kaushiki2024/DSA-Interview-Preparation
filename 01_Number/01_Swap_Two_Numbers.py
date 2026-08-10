# Problem: Swap two numbers

# Approach 1: Using a third variable
# Time Complexity: O(1)
# Space Complexity: O(1)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swapping using third variable:")
print("a =", a)
print("b =", b)


# Approach 2-1: Without using a third variable
# Time Complexity: O(1)
# Space Complexity: O(1)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping without third variable:")
print("a =", a)
print("b =", b)

# Approach 2-2: Without using a third variable ( Using XOR)
# Time Complexity: O(1)
# Space Complexity: O(1)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping using XOR:")
print("a =", a)
print("b =", b)