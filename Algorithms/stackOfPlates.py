"""
implement ds SetOfStacks that mimics if one stack pass threshhold move to another
composed of several stacks and create a new stack
push and pop should be the same as single stack

popAt(index) -> pops on specific sub stack
"""
def main():
    test = stackOfPlates()

    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    test.push(5)
    test.push(6)

    print "pop"
    print test.pop()

    print "POP AT"
    print test.popAt(2)

    print "***********"
    print "current stack", test.curr.stack
    print "current stack count", test.curr.marker

class stackNode:
    def __init__(self, marker):
        self.stack = []
        self.marker = marker
        self.next = None

class stackOfPlates:
    def __init__(self):

        """
        didnt need a linked list just a list since i can get pos easily
        """
        self.node_stack = stackNode(0)
        self.threshhold = 2
        self.curr = self.node_stack

    def push(self, x):
        print "current", self.curr
        print "current", self.curr.stack
        print "current", self.curr.marker
        print "current", self.curr.next

        if len(self.curr.stack) >= self.threshhold:
            new_stack_node = stackNode(self.curr.marker + 1)
            self.curr = new_stack_node
            new_stack_node.stack.append(x)
        else:
            self.curr.stack.append(x)

    def pop(self):
        # take the curr stack and pop
        return self.curr.stack.pop()

    def popAt(self, index):
        # search to find the index stack and then pop from it

        print "*", self.node_stack.marker
        print "**", self.node_stack.next.marker
        # this should return 2
        print "***", self.node_stack.next.next.marker

        # print self.curr.marker
        # print self.node_stack.marker
        # print "next marker", self.node_stack.next.marker
        # print "next next", self.node_stack.next.next
        #
        # while self.node_stack.marker != index:
        #     # keep moving
        #     print "moving", self.node_stack.marker
        #     self.node_stack = self.node_stack.next
        #
        # print "finally here", self.node_stack.marker

if __name__ == '__main__':
    main()
