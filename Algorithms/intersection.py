"""
given 2 lists, check if they intersect

return intersecting node (based on reference not value)

ex.
if kth node of first list is the same as jth node of 2nd then they are intersecting
"""

from LinkedList import LinkedList
from LinkedList import Node

def main(list1, list2):
    print_list(list1)
    print "====="
    print_list(list2)

    print "*******"
    res = intersecting(list1, list2)
    if res != None:
        print res.data
    else:
        print "you sucks"

def intersecting(list1, list2):

    if list1 is None or list2 is None:
        return None

    i = list1.head
    j = list2.head
    my_set = set()

    while i:
        my_set.add(i.data)
        i = i.next

    while j:
        if j.data in my_set:
            return j
        j = j.next
    return None


def print_list(list):
    curr = list.head


if __name__ == '__main__':
    list1 = LinkedList()
    list1.add("a")
    list1.add("b")
    list1.add("d")
    list1.add("e")

    list2 = LinkedList()
    list2.add("d")
    list2.add("c")
    list2.add("b")
    list2.add("a")

    main(list1, list2)
