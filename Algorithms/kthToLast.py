"""
find the kth to last element of singly linked list

have runner b k in front of curr
move runner until the end of the list and then return curr
"""
from LinkedList import LinkedList

def main(list):
    printList(list)
    print "******"
    k = 4
    # print findkth(list, k).data
    head = list.head
    rec_findkth(head, k)

def findkth(list, k):
    curr = list.head
    i = 1
    runner = curr
    while i < k and runner:
        runner = runner.next
        i += 1

    while runner.next:
        curr = curr.next
        runner = runner.next

    return curr

# pass up the count until it hits k
def rec_findkth(head, k):
    if head == None:
        return 0
    count = rec_findkth(head.next, k) + 1
    if count == k:
        print head.data
    return count

def printList(list):
    curr = list.head
    while curr:
        print curr.data
        curr = curr.next
# what about 2 iters again
# runner is k away from the 1st and moves until it hits the end
# then return curr

if __name__ == '__main__':
    list = LinkedList()
    list.add(1)
    list.add(2)
    list.add(3)
    list.add(4)
    list.add(5)
    list.add(6)
    main(list)