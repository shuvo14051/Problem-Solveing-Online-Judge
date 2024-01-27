n = int(input())
word = input().upper()
result = ''
for i in word:
    asci = ord(i)
    asci += n
    if asci > ord('Z'):
            asci = (asci % ord('Z')) + ord('A') - 1
    ch = chr(asci)
    result += ch
print(result)

