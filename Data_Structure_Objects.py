class BinaryHeap:
    """
    Binary Heap is a class to implement a binary heap data structure.
    """

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self._queue[index][0] < self._queue[parent_index][0]:
            self._queue[index], self._queue[parent_index] = (
                self._queue[parent_index],
                self._queue[index],
            )
            index = parent_index
            parent_index = (index - 1) // 2

    def _sift_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_child_index = index
        if (
            left_child_index < len(self._queue)
            and self._queue[left_child_index][0] < self._queue[smallest_child_index][0]
        ):
            smallest_child_index = left_child_index
        if (
            right_child_index < len(self._queue)
            and self._queue[right_child_index][0] < self._queue[smallest_child_index][0]
        ):
            smallest_child_index = right_child_index
        if smallest_child_index != index:
            self._queue[index], self._queue[smallest_child_index] = (
                self._queue[smallest_child_index],
                self._queue[index],
            )
            self._sift_down(smallest_child_index)


class PriorityQueue(BinaryHeap):
    """
    Priority Queue is a class to implement a priority queue data structure using a binary heap.
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
        self._sift_up(len(self._queue) - 1)

    def update_priority(self, item, new_priority):
        """
        Updates the priority of an item in the queue.
        :param item: item whose priority is to be updated
        :param new_priority: new priority of the item
        """
        for i in range(len(self._queue)):
            if self._queue[i][1] == item:
                old_priority = self._queue[i][0]
                self._queue[i] = (new_priority, item)
                if new_priority < old_priority:
                    self._sift_up(i)
                else:
                    self._sift_down(i)

    def pop(self):
        """
        Pops the item with the highest priority from the queue.
        :return: item with the highest priority
        """
        if len(self._queue) == 0:
            raise ValueError("Queue is empty")
        entry = self._queue[0]
        last_entry = self._queue.pop()
        if len(self._queue) > 0:
            self._queue[0] = last_entry
            self._sift_down(0)
        return entry[1]

    def is_empty(self):
        """
        Checks if the queue is empty.
        :return: True if the queue is empty, False otherwise
        """
        if len(self._queue) == 0:
            return True


class HashTable:
    """
    HashTable is a class to implement a hash table data structure.
    """

    def __init__(self, rows):
        """
        Initialize the hash table with a given number of rows.
        :param rows: number of rows
        """
        self.size = self.next_prime(rows**2)
        self.table = [[] for _ in range(self.size)]

    @staticmethod
    def next_prime(n):
        """
        Find the next prime number after a given number.
        :param n: the given number
        :return: the next prime number
        """
        not_prime = []
        isprime = []

        for i in range(n + 1, n + 200):
            not_prime.append(i)

        for j in not_prime:
            val_is_prime = True
            for x in range(2, j - 1):
                if j % x == 0:
                    val_is_prime = False
                    break
            if val_is_prime:
                isprime.append(j)
        return min(isprime)

    def hash(self, tup):
        """
        Hash a given tuple to a corresponding index in the hash table.
        :param tup: the given tuple
        :return: the corresponding index in the hash table
        """

        hash_val = int((tup.x * self.size**0.5 + tup.y) % self.size)

        return hash_val

    def insert(self, tup):
        """
        Insert a given tuple into the hash table.
        :param tup: the tuple to be inserted
        """
        hash_val = self.hash(tup)
        self.table[hash_val].append(tup)

    def remove(self, tup):
        """
        Remove a given tuple from the hash table.
        :param tup: the tuple to be removed
        """
        hash_val = self.hash(tup)
        if tup in self.table[hash_val]:
            self.table[hash_val].remove(tup)
