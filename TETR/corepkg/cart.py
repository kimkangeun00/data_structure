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


    def remove_cart(self, product):

        if self.head is None:
            return

        # 첫 노드 삭제
        if self.head.data["id"] == product["id"]:

            self.head = self.head.next
            return

        prev = self.head
        current = self.head.next

        while current:

            if current.data["id"] == product["id"]:

                prev.next = current.next
                return

            prev = current
            current = current.next


    def clear_cart(self):

        self.head = None

    def count_product(self, product):

        count = 0

        current = self.head

        while current:

            if current.data["id"] == product["id"]:
                count += 1

            current = current.next

        return count