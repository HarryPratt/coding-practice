from bisect import bisect_right


def solution(A):
    pairs = 0

    # create an array of tuples, each containing the start and end indices of a disk
    # some indices may be less than 0 or greater than len(A), this is fine!
    # sort the array by the first entry of each tuple: the disk start indices
    intervals = sorted([(i - A[i], i + A[i]) for i in range(len(A))])

    # create an array of starting indices using tuples in intervals
    starts = [i[0] for i in intervals]

    # for each disk in order of the *starting* position of the disk, not the centre
    for i in range(len(starts)):

        # find the end position of that disk from the array of tuples
        disk_end = intervals[i][1]

        # find the index of the rightmost value less than or equal to the interval-end
        # this finds the number of disks that have started before disk i ends
        count = bisect_right(starts, disk_end)

        # subtract current position to exclude previous matches
        # this bit seemed 'magic' to me, so I think of it like this...
        # for disk i, i disks that start to the left have already been dealt with
        # subtract i from count to prevent double counting
        # subtract one more to prevent counting the disk itsself
        count -= i + 1
        pairs += count
        if pairs > 10000000:
            return -1
    return pairs


print(solution([1, 5, 2, 1, 4, 0]))
