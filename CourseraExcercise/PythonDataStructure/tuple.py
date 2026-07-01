""" Write a program to read through the mbox-short.txt
and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time
and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below."""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    
    # 1. Grab the time string (the 6th element, index 5) -> "09:14:16"
    time_str = words[5]
    
    # 2. Split the time string by the colon to isolate the hour -> ["09", "14", "16"]
    time_parts = time_str.split(":")
    hour = time_parts[0]
    
    # 3. Accumulate counts for each hour
    counts[hour] = counts.get(hour, 0) + 1

# 4. Convert dictionary items to a list of tuples and sort them by key (hour)
sorted_hours = sorted(counts.items())

# 5. Print the sorted key-value pairs matching the Desired Output
for hour, count in sorted_hours:
    print(hour, count)