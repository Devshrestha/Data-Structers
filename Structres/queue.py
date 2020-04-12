from linked_lists import node,ll_start

def add():
    value = input("Enter the value of element:")
    if start.head == None:
        start.head=node(value)
        return

    loop = start.head
    while loop.next:
        loop=loop.next
    added=node(value)
    loop.next=added

def remove():
    value = start.head.data
    start.head = start.head.next
    print(f"Removing from top of queue with value:{value}")

if __name__ == '__main__':
    start = ll_start()

    add()
    add()
    add()
    
    start.print_list()
    remove()
    start.print_list()