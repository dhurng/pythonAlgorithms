"""
check if list is palindrome
"""

from LinkedList import LinkedList
from LinkedList import Node

def main(list1):
    print_list(list1)

    print "*******"
    global length
    global mid
    length = list1.size()
    mid = length/2
    print is_pali(list1.head, mid)

def is_pali(head, count):
    curr = head

    if count == 0:
        if length % 2 != 0:
            return curr.next
        else:
            return curr

    count -= 1
    j = is_pali(curr.next, count)

    if j is None:
        return False

    print j.data
    print curr.data

    if j.data == curr.data:
        return j.next
    else:
        exit

def reverse_list(curr, prev):
    next = curr.next
    curr.next = prev
    if next is None:
        return curr
    else:
        return reverse_list(next, curr)

    # recurse until you reach the middle of the list
    # once in the middle then pass head.next so that will compare to the one bouncing back


def print_list(list):
    curr = list.head
    while curr:
        print curr.data
        curr = curr.next

if __name__ == '__main__':
    list1 = LinkedList()
    list1.add("a")
    list1.add("b")
    list1.add("d")
    list1.add("e")
    list1.add("d")
    main(list1)
