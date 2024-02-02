signal = input()
result = ""

i = 0
while i < len(signal) - 1:
    if signal[i] == "-" and signal[i+1] == ".":
        result += '1'
        i += 2  # Incrementing the index to skip the next character
    elif signal[i] == "-" and signal[i+1] == "-":
        result += '2'
        i += 2  # Incrementing the index to skip the next character
    elif signal[i] == ".":
        result += "0"
        i += 1  # Incrementing the index for the next iteration if "." is detected
    else:
        i += 1  # Incrementing the index if none of the conditions are met

# Handle the last character separately
if i == len(signal) - 1:
    if signal[i] == ".":
        result += "0"
    elif signal[i] == "-":
        result += '2'

print(result)