#Parsing and Extracting
#From stephen.marquard@uct.ac.za sat jan 5 9:14:16 2008

# Parsing and Extracting
data = "stephen.marquard@uct.ac.za sat jan 5 9:14:16 2008"

# 1. Find the index of the '@' symbol (usually what we look for in emails!)
# Note: If you specifically want the first "a", change "@" back to "a"
a = data.find("@")
print("Position of @:", a)

# 2. Find the first space AFTER the position of 'a'
b = data.find(" ", a)
print("Position of next space:", b)

# 3. Slice the string from just after 'a' up to 'b' to get the domain
c = data[a+1:b]
print("Extracted domain:", c)
