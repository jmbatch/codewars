def pick_peaks(arr):
    last, curr = 0, 0
    peak = []
    pos = []

    for next in range(1, len(arr)):
        if arr[next] > arr[curr]:
            last = curr
            curr = next
        else:
            if arr[next] < arr[curr]:
                if arr[last] < arr[curr]:
                    pos.append(curr)
                    peak.append(arr[curr])
                last = curr
                curr = next
    return {"pos": pos, "peaks": peak}
