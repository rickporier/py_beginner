def area(length, width=10):
    return length * width   # return, don’t print

def perimeter(length, width=10):
    return 2 * (length + width)

# Example 1: Just print results
print("Area:", area(5, 4))
print("Perimeter:", perimeter(5, 4))

# Example 2: Use results in math
total = area(5, 4) + perimeter(5, 4)
print("Area + Perimeter =", total)

# Example 3: Store results for later use
a = area(7, 3)
p = perimeter(7, 3)

if a > p:  # You can now use the values logically
    print("Area is larger than perimeter")
else:
    print("Perimeter is larger or equal")
