import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued {item} | Queue: {self.items}")

    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued {removed} | Queue: {self.items}")
            return removed
        else:
            print("Queue is empty. Nothing to dequeue.")
            return None
        
    def peek(self):
        if not self.is_empty():
            print(f"Front of queue: {self.items[0]}")
            return self.items[0]
        else:
            print("Queue is empty. No front item.")
            return None
        
    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        # TODO: Implement winner selection and dequeue process
        win_num = random.randint(0, len(self.items) - 1)
        for i in range(0, win_num):
            self.dequeue()
        return self.dequeue()
