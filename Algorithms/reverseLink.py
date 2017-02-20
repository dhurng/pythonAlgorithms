"""
reverse a linked list
"""
from LinkedList import LinkedList

def main(list):
    reverse(list)

def reverse(list):
    head = list.head


#     the current next is equal to the prev
#   the previous is equal to the forward

if __name__ == '__main__':
    list = LinkedList()
    list.add(1)
    list.add(2)
    list.add(3)
    list.add(4)
    print list
    main(list)