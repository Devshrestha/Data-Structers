from linked_lists import node,ll_start

def push(value):
    #print("[push operation]")
    #value = input("Enter the value of element:")
    if start.head == None:
        start.head=node(value)
        return

    loop = start.head
    while loop.next:
        loop=loop.next
    added=node(value)
    loop.next=added

def pop():
    if start.head.next==None:
        #print(f"[pop operation]\n removed node with value: {start.head.data}")
        start.head=None
        return
    prev=start.head
    loop=prev.next
    while (loop.next):
        loop=loop.next
        prev=prev.next
    prev.next=None
    #print(f"[pop operation]\n removed node with value: {loop.data}")



if __name__ == '__main__':
    start = ll_start()
    push(46)
    push(4)
    start.print_list()
    pop()
    pop()
    start.print_list()