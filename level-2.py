class intervals:
    def __init__(self):
        # List to store intervals
        self.intervals = []

    def addInterval(self, a, b):
        #Adds a new interval and merges overlapping intervals
        self.intervals.append([a, b])
        self.intervals.sort()

        merged = []
        for i in self.intervals:
            start = i[0]
            end = i[1]
            if merged and merged[-1][1] >= start:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        self.intervals = merged

    def getIntervals(self):
        #Returns the merged list of intervals
        print(self.intervals)

# Example usage
interval1 = intervals()
interval1.addInterval(9, 11)
interval1.addInterval(1, 5)
interval1.addInterval(6, 8)
interval1.addInterval(4, 7)
interval1.addInterval(2, 5)
interval1.addInterval(6, 9)
interval1.addInterval(1, 7)
interval1.addInterval(4, 10)
interval1.addInterval(0, 2)

interval1.getIntervals()