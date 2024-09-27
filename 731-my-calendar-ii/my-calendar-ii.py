class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for overlap_start, overlap_end in self.overlaps:
            if start < overlap_end and end > overlap_start:
                return False
        for curr_start, curr_end in self.booked:
            if start < curr_end and end > curr_start:
                self.overlaps.append((max(start, curr_start), min(end, curr_end)))
        self.booked.append((start, end))
        return True
