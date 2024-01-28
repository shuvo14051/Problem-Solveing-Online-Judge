n = int(input())
my_set = set(map(int, input().split()))
number_of_sets_operations = int(input())

for i in range(number_of_sets_operations):
    operations, length = input().split()

    operation_set = set(map(int, input().split()))

    if operations == "intersection_update":
        my_set.intersection_update(operation_set)

    elif operations == "update":
        my_set.update(operation_set)

    elif operations == "symmetric_difference_update":
        my_set.symmetric_difference_update(operation_set)
   
    elif operations == "difference_update":
        my_set.difference_update(operation_set)


print(sum(my_set))


