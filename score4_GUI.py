# SCORE 4 - GRAPHICAL USER INTERFACE - PROPSATHEIA 2

from tkinter import *
from tkinter import messagebox
#import randoM

from bitarray import bitarray


class GameState:

    def __init__(self,master):
        self.master=master
        self.w=7
        self.library={}
        #self.rec=0
        self.remaining=42
        self.h=6
        self.board=[]
        self.index=0
        self.depth=3
        
        self.winner=-1
        self.action=-1
        self.flag=0
        for i in range(7):
            l=[]
            for j in range(6):
                l.append(' ')
            self.board.append(l)

            
    def example(self):
        self.move(2,0)
        self.move(1,1)
        self.move(3,0)
        self.move(2,1)
        self.move(4,0)
        

    def quit(self):

        file=open('score4_library.txt','a')

        for x in self.library:
            file.write(x+':'+self.library[x]+'\n')
        file.close()
        
        self.master.destroy()

    def play_ai(self):
        a=self.generate_move()
        self.move(a,1)
        self.update()
        self.remaining=self.remaining-1
        y=self.terminal()
        if y==True:
            messagebox.showinfo("info","THE GAME ENDS")
            self.frame.quit()
        

    def button_move(self,k):

        self.index=0# 0=human , 1=ai
        x=self.move(k,0)#this line changes the board state
        if x=="invalid move":
            return None
        self.update()#this line displays the new beard state
        y=self.terminal()
        if y==True:
            messagebox.showinfo("info","THE GAME ENDS")
            self.frame.quit()
        self.remaining=self.remaining-1
        return None

    def print(self):
        for i in range(6):
            for j in range(7):
                print(self.board[j][i]+'|',end=" ")
            print('\n')

    def move(self,column,index):# 0=human , 1=AI
        self.index=index

        if self.index==0:

            col=self.board[column-1]

            if col[5]==" ":
                self.board[column-1][5]='R'
            elif col[0]!=" ":
                messagebox.showinfo("info","INVALID MOVE")
                return("invalid move")
            else:
                p=0
                while self.board[column-1][p]==" ":
                    p=p+1
                self.board[column-1][p-1]='R'

        if self.index==1:

            col=self.board[column-1]

            if col[5]==" ":
                self.board[column-1][5]='G'
            elif col[0]!=" ":
                messagebox.showinfo("info","INVALID MOVE")
                return("invalid move")
            else:
                p=0
                while self.board[column-1][p]==" ":
                    p=p+1
                self.board[column-1][p-1]='G'

        return None


    def undom(self,column):
        col=column-1
        p=0
        while self.board[col][p]==" ":
            p=p+1

        self.board[col][p]=" "
        self.winner=-1

    def terminal(self):
        for i in range(6):#ORIZONTIA
            for j in range(4):
                #print(self.board[j][i])
                if self.board[j][i]==self.board[j+1][i]==self.board[j+2][i]==self.board[j+3][i] and self.board[j][i] in {'R','G'}:
                    #print(True)
                    if self.board[j][i]=='R':
                        self.winner=0
                    else:
                        self.winner=1
                    return(True)
        for i in range(7):
            for j in range(3):
                if self.board[i][j]==self.board[i][j+1]==self.board[i][j+2]==self.board[i][j+3] and self.board[i][j] in {'R','G'}:
                    #print(True)
                    if self.board[i][j]=='R':
                        self.winner=0
                    else:
                        self.winner=1
                    return(True)
        for i in range(4):
            for j in range(3):
                if self.board[i][j]==self.board[i+1][j+1]==self.board[i+2][j+2]==self.board[i+3][j+3] and self.board[i][j] in {'R','G'}:
                    #print(True)
                    if self.board[i][j]=='R':
                        self.winner=0
                    else:
                        self.winner=1
                    return(True)
        for i in range(3,7):
            for j in range(3):
                if self.board[i][j]==self.board[i-1][j+1]==self.board[i-2][j+2]==self.board[i-3][j+3] and self.board[i][j] in {'R','G'}:
                    #print(True)
                    if self.board[i][j]=='R':
                        self.winner=0
                    else:
                        self.winner=1
                    return(True)
        #print(False)
        return(False)

    def getmoves(self):

        moves=[]

        for i in range(7):
            if self.board[i][0]==" ":
                moves.append(i+1)
        return(moves)

 
    def generate_move(self):
        if self.remaining<=22:
            self.depth=4
        
        actions=self.getmoves()
        v=float('inf')
        for a in actions:
            self.move(a,1)
            #k=self.minimax(0,0)
            k=self.alphabeta(0,0,float('-inf'),float('inf'))
            self.undom(a)
            if k<v:
                v=k
                best=a
        #print(self.board)
        #print(str(self.board))
        #print(str(best))
        #print(self.library)
        #self.library[str(self.board)]=str(best)
        return(best)

    def update(self):
        for i in range(7):
            for j in range(6):
                if self.board[i][j]==" ":
                    pass
                if self.board[i][j]=="R":
                    self.c[(i+1,j+1)].create_oval(0,90,90,0,fill="red",outline="yellow")
                    self.c[(i+1,j+1)].grid(row=j+1,column=i+1)
                    #canv=Canvas(self.frame,width=90,height=90,bg="magenta")
                    #canv.grid(row=1,column=1)
                    
                if self.board[i][j]=="G":
                    #cr=Canvas(root,width=90,height=90,bg="black")
                    self.c[(i+1,j+1)].create_oval(0,90,90,0,fill="green",outline="yellow")
                    self.c[(i+1,j+1)].grid(row=j+1,column=i+1)
                    #cr.grid(row=j+1,column=i+1)
        return None

    def ordered_moves(self):
        actions=self.getmoves()
        A=[]
        d={}
        l=[]
        for a in actions:
            self.move(a,1)
            e=self.evaluation()
            d[a]=e
            l.append(e)
            self.undom(a)
        #print(l)
        l.sort()
        #print(l)
        for x in l:
            for y in d:
                if d[y]==x:
                    A.append(y)
                    del d[y]
                    break
        #print("ordered moves")
        #print(A)
        return(A)
    

    def alphabeta(self,index,depth,a,b):#na efarmoso move ordering anti gia tin afksoysa seira 1,2,3,4,5,6,7
        #na koitazo prota tis kales kiniseis opos 1) synexeia diadon kai triadon kai 2) kopsimata toy antipaloy.....logika se kapoia synartisi [move_order]
        y=self.terminal()
        if y==True:
            if self.winner==0:
                return(1000)
            else:
                return(-1000)

        if depth==self.depth:
            return(self.evaluation2())

        if index==0:
            value=float('-inf')
            #actions=self.ordered_moves()
            actions=self.getmoves()
            A=[]
            for act in actions:
                A.append(act)
                self.move(act,0)
                value=max(value,self.alphabeta(1,depth,a,b))
                self.undom(act)
                a=max(a,value)
                if a>=b:
                    break
            #print(actions)
            #print(A)
            #if A==actions:
            #    print(False)
            #else:
            #    print(True)
            return value
        if index==1:
            value=float('inf')
            #actions=self.ordered_moves()
            actions=self.getmoves()
            for act in actions:
                self.move(act,1)
                value=min(value,self.alphabeta(0,depth+1,a,b))
                self.undom(act)
                b=min(b,value)
                if b<=a:
                    break
            return value
        
    

    def minimax(self,index,depth):
        y=self.terminal()
        if y==True or depth==self.depth:
            return(self.evaluation())
        if index==0:
            actions=self.getmoves()
            
            k=float('-inf')
            for a in actions:
                self.move(a,0)
                w=self.minimax(1,depth)
                if w>k:
                    k=w
                    #self.action=a
                self.undom(a)
            return(k)
        if index==1:
            actions=self.getmoves()
            
            k=float('inf')
            for a in actions:
                self.move(a,1)
                w=self.minimax(0,depth+1)
                if w<k:
                    k=w
                    #self.action=a
                self.undom(a)
            return(k)


    def evaluation(self):

        y=self.terminal()
        if y==True:
            if self.winner==0:
                return(1000)
            else:
                return(-1000)



        r2=0
        r3=0
        c2=0
        c3=0
        d1_2=0
        d1_3=0
        d2_2=0
        d2_3=0

        xr2=0
        xr3=0
        xc2=0
        xc3=0
        xd1_2=0
        xd1_3=0
        xd2_2=0
        xd2_3=0




        

        for i in range(6):#ORIZONTIA
            for j in range(6):
                if self.board[j][i]==self.board[j+1][i]=='R':
                    r2=r2+1
        for i in range(6):
            for j in range(5):
                if self.board[j][i]==self.board[j+1][i]==self.board[j+2][i]=='R':
                    r2=r2-1
                    r3=r3+1
                    
        for i in range(7):#KATAKORYFA
            for j in range(5):
                if self.board[i][j]==self.board[i][j+1]=='R':
                    c2=c2+1
        for i in range(7):
            for j in range(4):
                if self.board[i][j]==self.board[i][j+1]==self.board[i][j+2]=='R':
                    c2=c2-1
                    c3=c3+1
                    
        for i in range(6):#PANO ARISTERA PROS KATO DEKSIA
            for j in range(5):
                if self.board[i][j]==self.board[i+1][j+1]=='R':
                    d1_2=d1_2+1
        for i in range(5):
            for j in range(4):
                if self.board[i][j]==self.board[i+1][j+1]==self.board[i+2][j+2]=='R':
                    d1_2=d1_2-1
                    d1_3=d1_3+1
                    
        for i in range(6):#KATO ARISTERA PROS PANO DEKSIA
            for j in range(1,6):
                if self.board[i][j]==self.board[i+1][j-1]=='R':
                    d2_2=d2_2+1
        for i in range(5):
            for j in range(2,6):
                if self.board[i][j]==self.board[i+1][j-1]==self.board[i+2][j-2]=='R':
                    d2_2=d2_2-1
                    d2_3=d2_3+1
        



        for i in range(6):#ORIZONTIA
            for j in range(6):
                if self.board[j][i]==self.board[j+1][i]=='G':
                    xr2=xr2+1
        for i in range(6):
            for j in range(5):
                if self.board[j][i]==self.board[j+1][i]==self.board[j+2][i]=='G':
                    xr2=xr2-1
                    xr3=xr3+1
                    
        for i in range(7):#KATAKORYFA
            for j in range(5):
                if self.board[i][j]==self.board[i][j+1]=='G':
                    xc2=xc2+1
        for i in range(7):
            for j in range(4):
                if self.board[i][j]==self.board[i][j+1]==self.board[i][j+2]=='G':
                    xc2=xc2-1
                    xc3=xc3+1
                    
        for i in range(6):#PANO ARISTERA PROS KATO DEKSIA
            for j in range(5):
                if self.board[i][j]==self.board[i+1][j+1]=='G':
                    xd1_2=xd1_2+1
        for i in range(5):
            for j in range(4):
                if self.board[i][j]==self.board[i+1][j+1]==self.board[i+2][j+2]=='G':
                    xd1_2=xd1_2-1
                    xd1_3=xd1_3+1
                    
        for i in range(6):#KATO ARISTERA PROS PANO DEKSIA
            for j in range(1,6):
                if self.board[i][j]==self.board[i+1][j-1]=='G':
                    xd2_2=xd2_2+1
        for i in range(5):
            for j in range(2,6):
                if self.board[i][j]==self.board[i+1][j-1]==self.board[i+2][j-2]=='G':
                    xd2_2=xd2_2-1
                    xd2_3=xd2_3+1
        
            
        #TELIKOS YPOLOGISMOS TIS SYNARTISIS AKSIOLOGISIS GIA TON PAIKTI 0 , TON KOKKINO

        r=(r2+c2+d1_2+d2_2)+3*(r3+c3+d1_3+d2_3)-(xr2+xc2+xd1_2+xd2_2)-3*(xr3+xc3+xd1_3+xd2_3)

        return(r)

    def evaluation2(self):#plithos dinitika nikiforon tetradon

        r=0

        r_star=set()
        
        for i in range(6):#ORIZONTIA
            for j in range(4):
                l=[self.board[j][i],self.board[j+1][i],self.board[j+2][i],self.board[j+3][i]]
                if set(l).issubset({'R',' '}):
                    c=l.count('R')
                    if c==3:
                        for t in range(4):
                            if l[t]==' ':
                                x=( j+t , i )
                                r_star.add(x)
                    r=r+2*c
        for i in range(7):
            for j in range(3):
                l=[self.board[i][j],self.board[i][j+1],self.board[i][j+2],self.board[i][j+3]]
                if set(l).issubset({'R',' '}):
                    c=l.count('R')
                    if c==3:
                        for t in range(4):
                            if l[t]==' ':
                                x=( i , j+t )
                                r_star.add(x)
                    r=r+2*c
        for i in range(4):
            for j in range(3):
                l=[self.board[i][j],self.board[i+1][j+1],self.board[i+2][j+2],self.board[i+3][j+3]]
                if set(l).issubset({'R',' '}):
                    c=l.count('R')
                    if c==3:
                        for t in range(4):
                            if l[t]==' ':
                                x=( i+t , j+t )
                                r_star.add(x)
                    r=r+2*c
        for i in range(3,7):
            for j in range(3):
                l=[self.board[i][j],self.board[i-1][j+1],self.board[i-2][j+2],self.board[i-3][j+3]]
                if set(l).issubset({'R',' '}):
                    c=l.count('R')
                    if c==3:
                        for t in range(4):
                            if l[t]==' ':
                                x=( i-t , j+t )
                                r_star.add(x)
                    r=r+2*c
        
        k=0

        k_star=set()

        for i in range(6):#ORIZONTIA
            for j in range(4):
                l=[self.board[j][i],self.board[j+1][i],self.board[j+2][i],self.board[j+3][i]]
                if set(l).issubset({'G',' '}):
                    c=l.count('G')
                    if c==3:
                        for t in range(4):
                            if l[t]==' ':
                                x=( j+t , i )
                                k_star.add(x)
                    k=k+2*c
        for i in range(7):
            for j in range(3):
                l=[self.board[i][j],self.board[i][j+1],self.board[i][j+2],self.board[i][j+3]]
                if set(l).issubset({'G',' '}):
                    c=l.count('G')
                    if c==3:
                        for t in range(4):
                            if l[t]==' ':
                                x=( i , j+t )
                                k_star.add(x)
                    k=k+2*c
        for i in range(4):
            for j in range(3):
                l=[self.board[i][j],self.board[i+1][j+1],self.board[i+2][j+2],self.board[i+3][j+3]]
                if set(l).issubset({'G',' '}):
                    c=l.count('G')
                    if c==3:
                        for t in range(4):
                            if l[t]==' ':
                                x=( i+t , j+t )
                                k_star.add(x)
                    k=k+2*c
        for i in range(3,7):
            for j in range(3):
                l=[self.board[i][j],self.board[i-1][j+1],self.board[i-2][j+2],self.board[i-3][j+3]]
                if set(l).issubset({'G',' '}):
                    c=l.count('G')
                    if c==3:
                        for t in range(4):
                            if l[t]==' ':
                                x=( i-t , j+t )
                                k_star.add(x)
                    k=k+2*c

        for x in r_star:
            for y in r_star-{x}:
                if x[0]==y[0]:
                    if ((x[1]-y[1])%2)==1:
                        r=r+10

        for x in k_star:
            for y in k_star-{x}:
                if x[0]==y[0]:
                    if ((x[1]-y[1])%2)==1:
                        k=k+10
                
        
        return(r-k)
    



def main():

    #EPOMENO VIMA NA FTIAKSO TO PROVLIMA ME BITBOARD !!!

    root=Tk()

    gs=GameState(root)

    gs.library={}#argotera tha xrisimopoio to eksoteriko file gia na arxizei me times.

    gs.frame=Frame(gs.master)
    gs.frame.pack()

    gs.c={}

    for i in range(1,8):# i : columns , j :rows
        for j in range(1,7):
            gs.c[(i,j)]=Canvas(gs.frame,width=90,height=90,bg="blue")
            gs.c[(i,j)].create_oval(0,90,90,0,fill="black")
            gs.c[(i,j)].grid(row=j,column=i)

    gs.b1=Button(gs.frame,text="1",fg="magenta",bg='blue' , command=lambda: gs.button_move(1))
    gs.b2=Button(gs.frame,text="2",fg="magenta",bg='blue' , command=lambda: gs.button_move(2))
    gs.b3=Button(gs.frame,text="3",fg="magenta",bg='blue' , command=lambda: gs.button_move(3))
    gs.b4=Button(gs.frame,text="4",fg="magenta",bg='blue' , command=lambda: gs.button_move(4))
    gs.b5=Button(gs.frame,text="5",fg="magenta",bg='blue' , command=lambda: gs.button_move(5))
    gs.b6=Button(gs.frame,text="6",fg="magenta",bg='blue' , command=lambda: gs.button_move(6))
    gs.b7=Button(gs.frame,text="7",fg="magenta",bg='blue' , command=lambda: gs.button_move(7))

    gs.q=Button(gs.frame,text="quit",fg="black",bg="white",command=gs.quit)
    gs.q.grid(row=0,column=10)

    gs.ai_button=Button(gs.frame,text="AI",bg='white',fg='black',command=gs.play_ai)
    gs.ai_button.grid(row=4,column=10)

    gs.b1.grid(row=0,column=1)
    gs.b2.grid(row=0,column=2)
    gs.b3.grid(row=0,column=3)
    gs.b4.grid(row=0,column=4)
    gs.b5.grid(row=0,column=5)
    gs.b6.grid(row=0,column=6)
    gs.b7.grid(row=0,column=7)

    root.mainloop()

#def create_library():
#    file=open('score4_library.txt','w')
#    file.close()
