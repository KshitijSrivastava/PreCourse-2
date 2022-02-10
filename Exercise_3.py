# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        
  
    def push(self, new_data):
        #pushing data at the head of the root
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        return

        
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        #initilize fast and slow pointer
        temp1 = self.head
        temp2 = self.head

        #continue to advance both the pointers till fast pointer has node to the next of next
        while temp2.next and temp2.next.next:
            temp1 = temp1.next
            temp2 = temp2.next.next
        print(temp1.data)



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
