class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        temp = set()
        temp.add(0)
        for _ in range(10):
            for i in range(len(rooms)):
                if i in temp:
                    temp.update(rooms[i])
        return len(temp) == len(rooms)
