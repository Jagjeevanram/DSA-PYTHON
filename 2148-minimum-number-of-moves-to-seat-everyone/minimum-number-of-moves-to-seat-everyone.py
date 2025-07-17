class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        place=0
        for i in range(len(seats)):
            place+=abs(seats[i]-students[i])
        return place    
