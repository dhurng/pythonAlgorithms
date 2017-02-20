"""
Linked List implementation

"""
def main():
    test = LinkedList()

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

    def get_data(self):
         return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList(object):

    def __init__(self, head = None):
        self.head = head


    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        pass

    def remove(self, data):
        current = self.head
        prev = None
        while current:
            if current.get_data == data:
                prev = current.get_next()
                current.set_next(None)
            else:
                prev = current
                current = current.get_next()

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        while current:
            if current.get_data() == data:
                return current
            else:
                current = current.get_next()
        print "not found"
        return False

    # class Node(object):
    #     def __init__(self, data = None, next_node = None):
    #         self.data = data
    #         self.next_node = next_node
    #
    #     def get_data(self):
    #         return self.data
    #
    #     def get_next(self):
    #         return self.next_node
    #
    #     def set_next(self, new_next):
    #         self.next_node = new_next

if __name__ == '__main__':
    main()
