# Task 4: Number Analyzer
# Scenario: Build a tool to analyze numbers entered by the user.

# Instructions:

# - Let the user enter up to 5 numbers (use a loop).
# - For each number:
#     - Check if it's even or odd.
#     - Check if it's positive, negative, or zero.
#     - Print the result for each.
# - After all entries, show how many:
#     - Were even
#     - Were odd
#     - Were negative
#     - Were zero

even = 0
odd = 0
negative = 0
zero = 0

for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))

    if number == 0:
        print("Zero")
        zero += 1
    elif number < 0:
        print("Negative")
        negative += 1
    else:
        print("Positive")

    if number != 0:
        if int(number) % 2 == 0:
            print("Even")
            even += 1
        else:
            print("Odd")
            odd += 1

print("\nSummary:")
print("Even:", even)
print("Odd:", odd)
print("Negative:", negative)
print("Zero:", zero)