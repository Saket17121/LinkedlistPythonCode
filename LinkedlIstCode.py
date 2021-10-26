#definition of a Linked List Node
class node :
    def __init__(self, data):
        self.data = data
        self.next = None

#Add an element in linked list at given index

    def push(self, d, n):
        new_node = node(d)
        if self.next is None:
            self.next = new_node
            return
        temp = self
        c=2
        while (temp):
            if(c==n) :
                new_node.next = temp.next
                temp.next = new_node
                return
            else :
                temp = temp.next
                c = c+1

#Add an Element at the end of the list

    def insertLast(self,d):
        new_Node = node(d)
        if self.next is None:
            self = new_Node
            return
        temp = self.next
        while(temp.next):
            temp = temp.next
        temp.next = new_Node

#Delete a node

    def pop(self,d):
        if self.next is None :
            return
        temp=self
        while(temp):
            if(temp.next.data ==  d):
                temp.next = temp.next.next
                return
            temp = temp.next

#traversal of the Linked List

    def printlist(self):
        temp = self
        while(temp) :
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == '__main__':
    g = node(1)
    g.printlist()
    g.push(2,2)
    g.push(3,3)
    g.push(4,4)
    g.push(5,5)
    g.printlist()
    g.push(8,2)
    g.pop(3)
    g.printlist()
    g.pop(5)
    g.printlist()
    g.insertLast(6)
    g.printlist()
