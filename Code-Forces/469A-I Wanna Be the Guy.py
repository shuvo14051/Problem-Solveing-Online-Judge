# n = int(input())

# levels1 = list(map(int, input().split()))
# levels2 = list(map(int, input().split()))

# finals = levels1+levels2

# if 0 in finals:
#     finals.remove(0)

# final_unique = set(finals)

# if len(final_unique) == n:
#     print("I become the guy.")

# else:
#     print("Oh, my keyboard!")


n = int(input())

# Levels Little X can pass
x_levels = set(map(int, input().split()[1:]))

# Levels Little Y can pass
y_levels = set(map(int, input().split()[1:]))

all_levels = set(range(1, n + 1))

# Check if the union of Little X and Little Y levels covers all levels
if all_levels.issubset(x_levels.union(y_levels)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
