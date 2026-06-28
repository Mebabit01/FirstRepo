#log_message = "ERROR: User 4022 failed to purchase item PID-98234 at 10:42 AM"
"""Your Tasks:
1. Find the position where the text "PID-" starts.

2. Find the position of the blank space " " that comes after the Product ID number.

3. Slice the string to extract just the numeric ID (98234), without the "PID-" prefix and without the trailing space.

4. Print your result.
"""

data = "ERROR: User 4022 failed to purchase item PID-98234 at 10:42 AM"
"""a = data.find("PID-")
print("The position of p: ", a)

b = data.find(" ", a)
print("Space after P: ", b)

c = data[a+4:b]
print("Result is: ", c)"""

#Another method with split()

words = data.split()

for word in words:
    if word.startswith("PID-"):
        result = word.replace("PID-", "")
        print("Result using split: ", result)
