n = int(input())
li = set(map(int, input().split()))
number_of_operations = int(input())
for i in range(number_of_operations):
    operations = input()
    operation_value_li = operations.split()
    if len(operation_value_li) == 1:
        li.pop()
    else:
        if operation_value_li[0] == 'discard':
            li.discard(int(operation_value_li[1]))
        elif operation_value_li[0] == 'remove':
            li.remove   (int(operation_value_li[1]))

print(sum(li))