import heapq

class SeatManager:

    def __init__(self, n: int):
        self.heap = list(range(1, n + 1))
        heapq.heapify(self.heap)

    def reserve(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


# Time limit Exceded
        
"""
class SeatManager:

    def __init__(self, n: int):
        self.seats = list( range(1,n+1))

    def reserve(self) -> int:
        if self.seats:
            return self.seats.pop(0)

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber not in self.seats:
            self.seats.append(seatNumber)
            self.seats.sort()
"""