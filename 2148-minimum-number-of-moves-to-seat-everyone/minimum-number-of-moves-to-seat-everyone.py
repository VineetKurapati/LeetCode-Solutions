class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        seats = sorted(seats)
        students = sorted(students)
        count = 0
        for i in range(n):
            seat = seats[i]
            student = students[i]
            temp = abs(seat - student)
            count += temp
        return count