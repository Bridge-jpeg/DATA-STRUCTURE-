# Name: Lyndo M. Lusac
# Description: This program gets the mid point from the given data that the user inputed
# Date of submission: 05/13/2025

class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LL():
    def __init__ (self):
        self.head = None

    def append(self, data):
        new_data = Node(data)
        if self.head == None:
            self.head = new_data
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_data

    def mid_point(self):
        fast_current = self.head
        slow_current = self.head
        while fast_current and fast_current.next:
            slow_current = slow_current.next
            fast_current = fast_current.next.next
        return print(slow_current.data)
        

ll = LL()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)

ll.mid_point()