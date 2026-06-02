from datetime import datetime


class OrderNode:

    def __init__(self, data):

        self.data = data
        self.next = None


class OrderQueue:

    def __init__(self):

        self.front = None
        self.rear = None


    def enqueue(self, order):

        new_node = OrderNode(order)

        if self.rear is None:

            self.front = new_node
            self.rear = new_node

            return

        self.rear.next = new_node
        self.rear = new_node


    def get_orders(self):

        orders = []

        current = self.front

        while current:

            orders.append(current.data)

            current = current.next

        return orders