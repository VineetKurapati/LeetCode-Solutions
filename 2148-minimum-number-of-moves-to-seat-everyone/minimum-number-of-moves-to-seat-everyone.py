class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = len(seats)
        count = 0
        for i in range(n):
            seat = seats[i]
            student = students[i]
            count += abs(seat - student)
        return count
    