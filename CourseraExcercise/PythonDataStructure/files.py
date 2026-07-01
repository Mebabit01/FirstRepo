"""Write a program that prompts for a file name, then opens that file and reads through the file, 
looking for lines of the form:  X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you
are testing below enter mbox-files.txt as the file name."""

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
total_value = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    # 1. Find where the number begins by slicing right after the colon
    colon_pos = line.find(":")
    number_str = line[colon_pos + 1:]
    
    # 2. Convert the isolated string portion into a floating-point number
    value = float(number_str.strip())
    
    # 3. Accumulate total and update counter
    total_value = total_value + value
    count = count + 1

# 4. Compute the average and print according to the Desired Output format
average = total_value / count
print("Average spam confidence:", average)