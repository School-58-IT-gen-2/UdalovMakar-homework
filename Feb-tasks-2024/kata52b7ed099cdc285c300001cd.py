def sum_of_intervals(intervals: list):
    len_ = 0
    intervals = list(sorted(intervals, key=lambda x: -(x[1] - x[0])))
    len_ = sum([i[1] - i[0] for i in intervals])
    if len(intervals) == 1: return intervals[0][1] - intervals[0][0]
    for interval in intervals:
        for l_interval in intervals[:intervals.index(interval)]:
            if interval[0] <= l_interval[1] and interval[0] >= l_interval[0]: len_ += interval[0] - min(interval[1], l_interval[1])
            if interval[1] <= l_interval[1] and interval[1] >= l_interval[0]: len_ += max(interval[0], l_interval[0]) - interval[1]
    return len_

sum_of_intervals([
   [1, 4], [7, 10], [3, 5]
])