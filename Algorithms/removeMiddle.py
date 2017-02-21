"""
remove middle node, not exactly the middle but
not the end or the beginning

given only access to that particular node
"""
from LinkedList import LinkedList
from LinkedList import Node

def main(list):
    printList(list)
    remNode = list.search("d")
    remMid(remNode)
    print "*******"
    printList(list)

def remMid(remNode):
    if remNode == None || remNode.next == None:
        return False

    next = remNode.next

    print next
    remNode.data = next.data
    remNode.set_next(next.next)

def printList(list):
    curr = list.head
    while curr:
        print curr.data
        curr = curr.next

if __name__ == '__main__':
    list = LinkedList()
    list.add("f")
    list.add("e")
    list.add("d")
    list.add("c")
    list.add("b")
    list.add("a")
    main(list)
