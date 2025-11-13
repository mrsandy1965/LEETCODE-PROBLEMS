import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.taskDictionary = {}
        for u,t,p in tasks :
            self.add(u,t,p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.heap , (-priority , -taskId , userId))
        self.taskDictionary[taskId] = (userId, priority)

    def edit(self, taskId: int, newPriority: int) -> None:
        oldUserId = self.taskDictionary[taskId][0]
        heapq.heappush(self.heap , (-newPriority , -taskId , oldUserId))
        self.taskDictionary[taskId] = (oldUserId , newPriority)


    def rmv(self, taskId: int) -> None:
        self.taskDictionary.pop(taskId)

    def execTop(self) -> int:
        highestPriorityTaskUserId = -1 
        while self.heap :
            priority,taskId,userId = heapq.heappop(self.heap)
            if -taskId in self.taskDictionary and self.taskDictionary[-taskId] == (userId , -priority):
                highestPriorityTaskUserId = userId
                self.taskDictionary.pop(-taskId)
                break
        return highestPriorityTaskUserId


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()