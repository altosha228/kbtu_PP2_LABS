from someFunctions import histogram, filterUnique, reverse_string

# Test histogram function
print("Histogram Test:")
histogram([4, 9, 7])
print()

# Test filterUnique function
print("Filter Unique Test:")
numbers = [2, 3, 4, 5, 3, 4, 2, 4]
print("Original list:", numbers)
print("Unique list:", filterUnique(numbers))
print()

# Test reverse_string function
print("String Reversal Test:")
text = "hello"
print(f"Original: {text}")
print(f"Reversed: {reverse_string(text)}")
