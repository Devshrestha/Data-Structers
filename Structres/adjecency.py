class adjnode:
    def __init__(self,data):
        self.data = data
        self.next=None



class Graph:

    def __init__(self,ver):
        self.ver=ver
        self.graph=[None]*ver

    def add_node(self,src,des):
        prev=self.graph[src]
        if prev==None:
            self.graph[src]={des}
        else:
            prev.add(des)
            self.graph[src]=prev

        prev=self.graph[des]
        if prev==None:
            self.graph[des]={src}
        else:
            prev.add(src)
            self.graph[des]=prev

    def add_edge(self,src,des):
        node=adjnode(des)
        node.next=self.graph[src]
        self.graph[src]=node

        node=adjnode(src)
        node.next=self.graph[des]
        self.graph[des]=node

    def print_list(self):
        for i in range(self.ver):
            temp=self.graph[i]
            print(f'Adjecency list of{i}:')
            while temp:
                print(' ->',temp.data)
                temp=temp.next



if __name__ == "__main__":
    v=Graph(10)
    v.add_edge(0,1)
    v.add_edge(0,4)
    v.add_edge(0,7)
    v.add_edge(0,9)
    v.add_edge(0,9)

    v.print_list()