class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class Cart:

    def __init__(self):

        self.head = None


    def add_cart(self, product):

        new_node = Node(product)

        if self.head is None:

            self.head = new_node
            return


        current = self.head

        while current.next:

            current = current.next


        current.next = new_node


    def get_items(self):

        items = []

        current = self.head

        while current:

            items.append(current.data)

            current = current.next

        return items