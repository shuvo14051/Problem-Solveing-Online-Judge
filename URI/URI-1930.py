# Read input values
t1, t2, t3, t4 = map(int, input().split())

# Calculate the total number of devices that can be connected
total_devices = t1 + t2 + t3 + t4 - 3  # Subtract 3 because each power strip has one built-in outlet

# Print the result
print(total_devices)
