"""
given a circular linked list, return a node at the beginning of the loop

ex.
a -> b -> c -> d -> e -> c
output: c
"""

from LinkedList import LinkedList
from LinkedList import Node

def main(list1):
    print_list(list1)

    print "*******"
    create_loop(list1)
    collide = loop_detect(list1)
    find_start(collide)

def create_loop(list1):
    curr = list1.head
    while curr.next:
        curr = curr.next
    curr.next = list1.search("c")

def loop_detect(list1):
    curr = runner = list1.head
    while(curr and runner and runner.next):
        curr = curr.next
        runner = runner.next.next

        if curr.data is runner.data:
            return curr
    print "No loop found"

def find_start(collide):
    curr = list1.head
    runner = collide
    print "head: ", curr.data
    print "collide and runner: ", runner.data

    if runner is None and runner.next is None:
        return False

    while curr is not runner:
        curr = curr.next
        runner = runner.next

    print curr.data
    return curr

    # find the point where they meet
    # reset the slow(curr) to the head and keep runner at the same position
    # check if they dont end by looking for runner and runner.next is None
    # iterate the iterators until they equal each other
    # return the potision

def print_list(list):
    curr = list.head
    while curr:
        print curr.data
        curr = curr.next

if __name__ == '__main__':
    list1 = LinkedList()

    list1.add("f")
    list1.add("e")
    list1.add("d")
    list1.add("c")
    list1.add("b")
    list1.add("a")
    main(list1)
