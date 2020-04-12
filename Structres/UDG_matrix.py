
def add(src,links,wei=1):
    for a in range(len(mat[src])):
        if a!=src:    
            if a == links:
                mat[src][a]=1*wei
            elif mat[src][a]!=0 and mat[src][a]!=None:
                pass
            else:
                mat[src][a]=0

def call(a,b,w=1):
    add(a,b,w)
    add(b,a,w)            



if __name__ == "__main__":
    
    length = int(input('Enter the number of vertices:'))
    mat=[]
    for i in range(length):
        a=[]
        for j in range(length):
            if j==i:
                a.append(None)
            else:    
                a.append(0)
        mat.append(a)
    call(0,1)
    call(2,0,5)
    print(mat)