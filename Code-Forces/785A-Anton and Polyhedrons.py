n = int(input())
count = 0

for i in range(n):
    line = input()

    if line == "Tetrahedron":
        count += 4
    elif line == "Cube":
        count += 6
    elif line == "Octahedron":
        count += 8
    elif line == "Dodecahedron":
        count += 12
    elif line == "Icosahedron":
        count += 20

print(count)
