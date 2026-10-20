class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head=None

    def get(self, index):
        temp = self.head
        i = 0

        while temp is not None:
            if i == index:
                return temp.val
            temp = temp.next
            i += 1

        return -1
        

    def addAtHead(self, val):
        
        new=Node(val)
        new.next=self.head
        self.head=new
        

    def addAtTail(self, val):
        new=Node(val)
        if self.head is None:
            self.head=new
            return
        temp=self.head
        while temp is not None and temp.next is not None:
            temp=temp.next
            
        temp.next=new
        

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return
        i = 0
        temp = self.head
        while temp is not None and i < index - 1:
            temp = temp.next
            i += 1
        if temp is None:
            return
        new = Node(val)
        new.next = temp.next
        temp.next = new
        

    def deleteAtIndex(self, index):
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        i = 0
        temp = self.head
        while temp.next is not None and i < index - 1:
            temp = temp.next
            i += 1
        if temp.next is not None:
            temp.next = temp.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)