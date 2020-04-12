class node:

    def __init__(self,data):
        self.data=data
        self.next=None

class ll_start:

    def __init__(self):
        self.head=None

    def print_list(self):
        temp = self.head
        if self.head==None:
            print('The list is empty')
        while (temp):
            print(temp.data)
            temp=temp.next

def add_front():
    value=input("Enter the head:")
    if first.head==None:
        first.head=node(value)
        return
    temp=first.head
    first.head=node(value)
    first.head.next=temp


def add_mid():
    value=input('Enter data of new node:')
    prev=input('Enter the value of previous node:')

    loop = first.head
    while loop:
        if loop.data == prev:
            break
        else:
            loop=loop.next
    else:
        print('No such previous node exist!!')
        return
    middle=node(value)
    middle.next=loop.next
    loop.next=middle
    
def add_end():
    value=input("Enter the data of last node:")
    endding=node(value)
    if first.head.next==None:
        first.head.next=endding
        return
    loop = first.head
    while loop.next:
        loop=loop.next
    loop.next=endding

def remove_front():
    value = first.head.data
    if first.head.next == None:
        first.head=None
    else:
        first.head = first.head.next
    print(f"Removing from top of list with value: {value}")

def remove_mid():
    value=input('Enter the value of node u want to remove:')
    prev = first.head   
    if prev.data==value:
        remove_front()
        return
    loop=prev.next
    while (loop.next):
        if loop.data==value:
            break
        else:
            loop=loop.next
            prev=prev.next
    prev.next=loop.next
    print(f"Removed the node with value: {value}")


def remove_end():
    if first.head.next==None:
        first.head=None
        return
    prev=first.head
    loop=prev.next
    while (loop.next):
        loop=loop.next
        prev=prev.next
    prev.next=None
    print(f"Removed the node with value: {loop.data}")

if __name__=='__main__':
    first=ll_start()
    add_front()
    while True:
        y=input("Do you wish to add another node(y/n):")
        if y in 'yY':
            listing=True
            break
        elif y in 'Nn':
            listing=False
            break
        else:
            print('Invalid input')
    while listing:
        print("Where u want to insert node")
        choice=input("front,mid or end(f/m/e):")
        
        if choice in 'fF':
           add_front()
        elif choice in 'mM':
            add_mid()
        elif choice in 'eE':
            add_end()
        else:
            print('!! Invalid input !!')
            continue 
        
        while True:
            x= input('Want to enter more?(y/n)')
            if x=='n' or x=='N':
                listing=False
                break
            elif x  in ['y','Y']:
                break
            else:    
                print("!!Invalid input(y/n)!!")

    
    print("The Linked list:")
    first.print_list()

    while True:
        y=input("Do you wish to remove any node(y/n):")
        if y in 'yY':
            removing=True
            break
        elif y in 'Nn':
            removing=False
            break
        else:
            print('Invalid input')
    while removing:
        print("Where u want to delete node from")
        choice=input("front,mid or end (f/m/e):")
        
        if choice in 'fF':
           remove_front()
        elif choice in 'mM':
            remove_mid()
        elif choice in 'eE':
            remove_end()
        else:
            print('!! Invalid input !!')
            continue 
        
        print("The Linked list:")
        first.print_list()
        
        if first.head==None:
            break 
        
        while True:
            x= input('Want to remove more?(y/n)')
            if x=='n' or x=='N':
                removing=False
                break
            elif x  in ['y','Y']:
                break
            else:    
                print("!!Invalid input(y/n)!!")
    

    