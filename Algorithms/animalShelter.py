"""
ds that can deq and enq from cat or dog list
can use linked list
"""

def main():
    test = q()
    dog1 = Node("a", "dog")
    dog2 = Node("b", "dog")
    cat1 = Node("c", "cat")
    cat2 = Node("d", "cat")

    test.nq(dog1)
    test.nq(cat1)
    test.nq(dog2)
    test.nq(cat2)

    print "==cat=="
    for i in test.qcat:
        print i.name, i.time
    print "==dog=="
    for j in test.qdog:
        print j.name, j.time

    print "first", test.dq_any().name
    print "dq dog", test.dq_dog().name
    print "dq cat", test.dq_cat().name

class Node:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.time = None
        # use this to create a linked list
        self.next = None

class q:
    global time

    def __init__(self):
        self.qcat = []
        self.qdog = []
        self.time = 0

    def nq(self, animal):
        self.time += 1
        animal.time = self.time
        if animal.type == "dog":
            # when append create the link
            self.qdog.append(animal)
        else:
            self.qcat.append(animal)

    # this returns the animal but doesnt pop!
    def dq_any(self):
        # check the top of whichever q and then compare the time
        # whichever is less return that
        if len(self.qcat) <= 0 and len(self.qdog) > 0:
            print "cat empty"
            return self.qdog[0]
        elif len(self.qdog) <= 0 and len(self.qcat) > 0:
            print "dog empty"
            # when returning the top return the head
            # curr = head
            # save = curr
            # curr = curr.next
            # head = curr
            return self.qcat[0]
        else:
            if self.qcat[0].time < self.qdog[0].time:
                return self.qcat[0]
            else:
                return self.qdog[0]

    def dq_dog(self):
        if len(self.qdog) > 0:
            return self.qdog[0]

    def dq_cat(self):
        if len(self.qcat) > 0:
            return self.qcat[0]

if __name__ == '__main__':
    main()
