"""
describe how to use a single array to implement 3 stacks
"""

def main():
    test = three_stack()
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    test.print_list()
    print "size ", test.get_size()
    print "pop", test.pop()
    print "empty", test.is_empty()

class three_stack:
    number_of_stacks = 3
    # number of elements per stack
    stackCapacity
    # the actual array to store elements
    values = []
    # store the indexes
    sizes = []

    def __init__(self, stackSize):
        stackCapacity = stackSize
        values = [stackSize * number_of_stacks]
        sizes = [number_of_stacks]

    def push(self, stackNum, item):
        if is_full(stackNum):
            print "full"
        sizes[stackNum += 1]
        values[index_of_top(stackNum)] = item

    def pop(self, stackNum):
        if is_empty(stackNum):
            print "empty"
        return values[index_of_top(stackNum)]

    def is_empty(self, stackNum):
        return sizes[stackNum] == 0

    def is_full(self, stackNum):
        return sizes[stackNum] == stackCapacity

    def index_of_top(self, stackNum):
        offset = stackNum * stackCapacity
        size = sizes[stackNum]
        return offset + size - 1

    def get_size(self):
        return self.count

    def print_list(self):
        for i in self.array:
            print i

if __name__ == '__main__':
    main()
