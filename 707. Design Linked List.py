class Node:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            print(self.size)
            return -1
        trav = self.head
        while index > 0:
            trav = trav.next
            index -= 1
        return trav.val



    def addAtHead(self, val: int) -> None:
        newHead = Node(val, self.head)
        self.head = newHead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newTail = Node(val)
        if not self.head:
            self.head = newTail
        else:
            trav = self.head
            while trav.next:
                trav = trav.next
            trav.next = newTail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            trav = self.head
            while index > 1:
                trav = trav.next
                index -= 1
            addNode = Node(val, trav.next)
            trav.next = addNode
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            trav = self.head
            while index > 1:
                trav = trav.next
                index -= 1
            trav.next = trav.next.next
        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
