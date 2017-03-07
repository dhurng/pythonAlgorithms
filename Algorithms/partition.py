"""
move all the nodes smaller than to the left
all the larger to the right
if the x is in there it just needs to be in the right partition

ex.
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 (partition = 5)
3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
from LinkedList import LinkedList
from LinkedList import Node

def main(list):
    printList(list)

    print "******"
    part = 5
    res = partition(list, part)
    printList(res)

def partition(list, part):
    curr = list.head
    left = LinkedList()
    right = LinkedList()

    while curr:
        if curr.data < part:
            left.add(curr.data)
        else:
            right.add(curr.data)
        curr = curr.next

    # append left and right
    leftI = left.head
    while leftI and leftI.next:
        leftI = leftI.next


    leftI.next = right.head

    return left

def partition2(list, part):
    curr = list.head
    head = curr
    tail = curr

    if curr == None or curr.next == None:
        return False

    while curr:
        if curr.data < part:
            curr.next = head
            head = curr
        else:
            curr.next = tail
            tail = curr
        curr = curr.next
    tail.next = None

    return head


def printList(list):
    curr = list.head
    while curr:
        print curr.data
        curr = curr.next

if __name__ == '__main__':
    list = LinkedList()
    list.add(1)
    list.add(2)
    list.add(10)
    list.add(5)
    list.add(8)
    list.add(5)
    list.add(3)
    main(list)
