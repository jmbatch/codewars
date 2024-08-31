def first_non_consecutive(arr):
    for curr in range(0, len(arr)-1):
        next = curr + 1
        if arr[next] - arr[curr] > 1:
            return arr[next]
            exit()
    return None
