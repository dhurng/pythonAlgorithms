"""
if numbers are in reverse add them
ex.
7->1->6 + 5->9->2 = 617 + 295
2 -> 1 -> 9 = 912

if numbers are in order add them
ex.
6->1->7 + 2->9->5->
9->1->2
"""

from LinkedList import LinkedList
from LinkedList import Node

def main(list1, list2):
    print "list1"
    print_list(list1)
    print "list2"
    print_list(list2)


    print "*******"
    global carry = 0
    res = sum_foreward(list1.head, list2.head)
    print_list(res)

def padder(trgt, amount):
    # trgt add the amount of 0s in front
    pass

def sum_foreward(l1, l2):
# padd them
    l1len = l1.size()
    l2len = l2.size()
    if l1len > l2len:
        padder(l2, l1len - l2len)
    else:
        padder(l1, l2len - l1len)

    sol = LinkedList()
    val = carry
    sum_helper(l1, l26, sol)

    if carry != 0:
        res.add(1)

    return sol

def sum_helper(l1, l2, sol):
    # base case
    if l1 is None and l2 is None:
        return None

    sum_helper(l1.next l2.next, sol)
    val = carry + l1.data + l2.data

    sol.add(val % 10)
    carry = val/10
    return sol

def add_list(list1, list2):
    i = list1.head
    j = list2.head
    res = LinkedList()
    flag = False

    while i and j:
        sum = i.data + j.data
        if flag:
            sum += 1
        if sum < 10:
            flag = False
            res.add(sum)
        else:
            flag = True
            res.add(sum % 10)

        i = i.next
        j = j.next

    if i is None:
        if flag:
            sum = j.data + 1
            res.add(sum)
            j = j.next
            flag = False
        while j:
            res.add(j.data)
            j = j.next

    # if j is None would be same, call a sep method?
    if j is None:
        if flag:
            sum = i.data + 1
            res.add(sum)
            i = i.next
            flag = False
        while i:
            res.add(i.data)
            i = i.next

    if i is None and j is None and flag:
        res.add(1)

    return res

def convert_int(list):
    curr = list.head
    num = []
    i = 0
    while curr:
        num.append(curr.data)
        curr = curr.next

    s = ''.join(map(str, num))
    print int(s)
    print type(int(s))

def sum_recursive(l1, l2, carry):
    # base case
    if l1 is None and l2 is None and carry == 0:
        return None

    res = LinkedList()
    val = carry
    if l1 is not None:
        val += l1.data
    if l2 is not None:
        val += l2.data
    res.add(val % 10)

    # recurse
    if l1 is not None or l2 is not None:
        more = Node()
        more = sum_recursive(l1 = l1.next if l1 is not None else None, l2 = l2.next if l2 is not None else None, val=1 if val >= 10 else 0)
        res.add(more)
    return res

def sum_of_list(head):
    curr = head
    if curr is None:
        return 0
    return curr.data + sum_of_list(curr.next)

# decide to print forward instead of backwards
def print_list(list):
    curr = list.head
    while curr:
        print curr.data
        curr = curr.next

# inner helper class
class partial_sum(object, self):
    def __init__(self):
        sum = LinkedList()
        carry = 0

def pad(list, pad_num):
    # add number of 0s for pad_num to front of list
    pass

def add_list_recurse(l1, l2, carry):
    # wouldnt work since these are nodes
    len1 = l1.size()
    len2 = l2.size()

    if len1 < len2:
        pad(l1, len2 - len1)
    if len1 > len2:
        pad(l2, len1 - len2)

    pass

if __name__ == '__main__':
    list1 = LinkedList()
    list1.add(8)
    list1.add(8)
    list1.add(7)
    list1.add(9)
    list1.add(5)

    list2 = LinkedList()
    list2.add(8)
    list2.add(1)
    list2.add(2)
    # list2.add(7)

    main(list1, list2)
