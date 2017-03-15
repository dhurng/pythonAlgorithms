"""
stack that has a min function to return the min element in O(1) operation
"""

def main():
    test = stackMin()
    test.push(5)
    test.push(6)
    test.push(3)
    test.push(7)
    test.pop()
    test.pop()
    print test.container
    print "*", test.smallest_list

    # test.pop()
    #
    # print test.container
    # print "*", test.smallest_list
    #
    # test.pop()
    #
    # print test.container
    # print "*", test.smallest_list

    print "min: ", test.min()

class stackMin:
    def __init__(self):
        self.container = []
        self.smallest_list = []
        self.smallest = 0

    def push(self, x):
        self.container.append(x)

        if len(self.container) == 1:
            self.smallest = self.container[0]
            self.smallest_list.append(self.container[0])

        elif x <= self.smallest:
            self.smallest = x
            self.smallest_list.append(x)

    def pop(self):
        if len(self.container) > 0:
            if self.container[-1] == self.smallest:
                print "smallest is leaving"
                self.smallest_list.pop()
                self.smallest = self.smallest_list[-1]
            # do you need to set the smallest to the next?
            # self.smallest = self.smallest_list[-2]
            return self.container.pop()
        return None

    def min(self):
        if len(self.smallest_list) > 0:
            return self.smallest
        return None

if __name__ == '__main__':
    main()
