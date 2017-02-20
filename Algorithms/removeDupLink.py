"""
remove duplicates from unsorted linked list

no temporary buffer
"""

from LinkedList import LinkedList

def main(list):
    printList(list)
    remove_dup2(list)
    printList(list)

def remove_dup(list):
    map = {}
    current = list.head

    while current:
        if current.data in map:
            list.remove(current)
        else:
            map[current.data] = 1
        current = current.get_next()

    print map
    for i in map:
        print i

def remove_dup2(list):
    current = list.head
    while current:
        runner = current
        while runner.next:
            if current.data == runner.next.data:
                print "SAME!"
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

def printList(list):
    current = list.head
    while current:
        print current.data
        current = current.next

if __name__ == '__main__':
    list = LinkedList()
    list.add(1)
    list.add(2)
    list.add(4)
    list.add(2)
    list.add(3)
    list.add(3)
    print list
    # 3, 3, 2, 1
    main(list)