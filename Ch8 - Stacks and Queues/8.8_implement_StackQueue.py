# Implement a queue using stacks

class StackQueue:

    def __init__(self, data, stack_1=[], stack_2=[]):
        # data would be list of input items
        self.stack_1 = stack_1
        self.stack_2 = stack_2
        self.data = data

        # Pushing initial data in stack_1
        for item in self.data:
            self.stack_1.append(item)


    def push(self, item):
        # pushing one item
        self.stack_1.append(item)



    def pop(self):
        if len(self.stack_2) == 0:
            # this is when the whole stackQueue is empty
            if len(self.stack_1) == 0:
                return 'The StackQueue is empty!'

            # case 1 scenario
            else:
                for i in range(0, len(self.stack_1)):
                    if(i != 0):
                        shift_item = self.stack_1.pop()
                        self.stack_2.append(shift_item)

                return self.stack_1.pop()

        else:
            return self.stack_2.pop()



    def peek(self):
        if len(self.stack_2) != 0:
            return self.stack_2[-1]

        else:
            if len(self.stack_1) != 0:
                return self.stack_1[-1]
            else:
                return 'The StackQueue is empty!'


    def isEmpty(self):
        if len(self.stack_1) == 0 and len(self.stack_2) == 0:
            return True


    def printQ(self):
        if self.isEmpty() == True:
            return 'The StackQueue is empty'

        else:
            if len(self.stack_2) == 0:
                return self.stack_1

            else:
                stack_print = []
                stack_temp = []

                for i in range(len(self.stack_2)-1, -1, -1):
                    stack_print.append(self.stack_2[i])

                if len(self.stack_1) != 0:
                    for i in range(len(self.stack_1)-1, -1, -1):
                        stack_temp.append(self.stack_1[i])

                    for i in range(len(stack_temp)):
                        item = stack_temp.pop()
                        stack_print.append(item)

                return stack_print


# initialise a new stackQueue
queue = StackQueue([1, 3, 5, 7])
print(queue.pop())
print(queue.printQ())

queue.push(9)
queue.push(13)
print(queue.printQ())

print(queue.pop())
print(queue.printQ())

print(queue.peek())
