class Queue:
    def __init__(self):
        self.queue = list()

    def addtoq(self, dataval):
        if dataval not in self .queue:
            self.queue.insert(0,dataval)
            return True
        return False

    def size(self):
        return len(self.queque)

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.size())