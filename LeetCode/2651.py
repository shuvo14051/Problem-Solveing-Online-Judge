class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        hour = arrivalTime + delayedTime

        if hour >= 24:
            return hour-24
        
        return hour
    
