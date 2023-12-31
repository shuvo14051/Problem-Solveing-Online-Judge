# Encryption
import re

test = int(input())
# baseline = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(test):
    result_text = ""
    second_half_shift = ""
    text = input()
    for char in text:
        if re.match("[a-zA-Z]", char):
            result_text += chr(ord(char)+3)
        else:
            result_text += char
    result_text = result_text[::-1]
    mid_point = len(result_text)//2
    first_half = result_text[0:mid_point]
    second_half = result_text[mid_point:]

    for ch in second_half:
        second_half_shift += chr(ord(ch)-1)
    print(first_half+second_half_shift)
