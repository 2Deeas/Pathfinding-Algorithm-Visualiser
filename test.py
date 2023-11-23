class PriorityQueue:
    """
    Priority Queue is a class to implement a priority queue data structure.
    """

    def __init__(self):
        """
        Initialize an empty queue.
        """
        self._queue = []

    def push(self, item, priority):
        """
        Pushes an item into the queue with a given priority.
        :param item: item to be added
        :param priority: priority of the item
        """
        entry = (priority, item)
        self._queue.append(entry)

    def pop(self):
        """
        Pops the item with the highest priority from the queue.
        :return: item with the highest priority
        """
        if len(self._queue) == 0:
            raise ValueError("Queue is empty")
        highest = 0
        for i in range(len(self._queue)):
            if self._queue[i][0] < self._queue[highest][0]:
                highest = i
        entry = self._queue[highest]
        del self._queue[highest]
        return entry[1]

    def is_empty(self):
        """
        Checks if the queue is empty.
        :return: True if the queue is empty, False otherwise
        """
        if len(self._queue) == 0:
            return True


class BinaryHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def pop(self):
        if len(self.heap) == 0:
            raise ValueError("Heap is empty")

        self.swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self.heapify_down(0)

        return item

    def heapify_down(self, i):
        while i < len(self.heap):
            min_index = i

            left = self.left_child(i)
            if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
                min_index = left

            right = self.right_child(i)
            if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
                min_index = right

            if i != min_index:
                self.swap(i, min_index)
                i = min_index
            else:
                break
