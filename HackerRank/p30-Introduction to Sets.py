def average(arr):
    li = set(arr)
    result = sum(li)/len(li)
    return result


if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    result = average(arr)
    print(result)