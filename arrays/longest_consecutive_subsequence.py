def subsequence(arr):
    longest = 0
    s = set(arr)

    for val in s:
        if (val - 1) not in s:
            cnt = 1
            curr = val

            while (curr + 1) in s:
                cnt += 1
                curr += 1

            longest = max(longest, cnt)

    return longest

print(subsequence([102, 4, 1, 101, 3, 9, 2, 1, 1]))
