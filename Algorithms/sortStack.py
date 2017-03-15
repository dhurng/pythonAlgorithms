"""
sort a stack, smallest items are on top
can use additional temp stack, but not copy elements into any other ds
push, pop, peek, isempty
"""

def main():
    test = sortStack()

    test.push(3)
    test.push(5)
    test.push(1)
    test.push(8)
    test.push(2)
    test.push(8)
    print "========"
    print test.stack
    # checks this is the head
    print test.stack.pop()
    print "empty ", test.is_empty()

class sortStack:
    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def push(self, data):
        # base case
        if len(self.stack) <= 0:
            print "empty so adding"
            self.stack.append(data)
        else:
            if self.stack[-1] >= data:
                print "adding"
                self.stack.append(data)
            else:
                print "sorting"
                while len(self.stack) > 0:
                    if self.stack[-1] < data:
                        self.temp_stack.append(self.stack.pop())

                        print self.stack
                        print "*", self.temp_stack
                    else:
                        break
                self.stack.append(data)

                print "final", self.stack
                # push back the stuff in temp
                while len(self.temp_stack) > 0:
                    self.stack.append(self.temp_stack.pop())

                print "final 2", self.stack

        print self.stack
        print self.temp_stack

    def pop(self):
        # will remove the smallest but the rest would be sorted
        pass

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return True if len(self.stack) <= 0 else False

if __name__ == '__main__':
    main()
