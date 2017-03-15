"""
implement a q class which implements a q using 2 stack
"""

def main():
    test = MyQueue()

    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)


    print test.pop()
    print test.pop()
    print test.stack1
    print test.stack2

    # print test.stack1
    #
    # print test.pop()
    # print "*****"
    # # shoudl return failure so need to shift stacks
    # print test.pop()
    #
    # print test.stack1

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # treat s1 as inbox
    def push(self, data):
        self.stack1.append(data)

    def pop(self):
        # if outbox (s2) is empty refill it with s1
        # return the top of s2 which is the q of s1
        # ultimately reverse the stack
        if len(self.stack2) <= 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

if __name__ == '__main__':
    main()
