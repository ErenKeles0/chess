import tkinter as tk
import images as i


window=tk.Tk()
window.title("Chess")
window.geometry("1000x800")
window.resizable(width=False, height=False)



basilan=0

class square():
    def __init__(self,color,rotateX,rotateY,images,id):
        self.id=id
        self.color=color
        self.basildimi=False
        self.rotatex=100+(rotateX*72)-36
        self.rotatey=100+(rotateY*72)-36
        self.img=images
        self.imagee=tk.PhotoImage(file=images)
        self.button=tk.Button(image=self.imagee,command=self.basildi1)
        self.button.place(width=72,height=72,x=self.rotatex,y=self.rotatey)

    def basildi1(self):
        global basilan

        if not ((self.img=="WB.png" or  self.img=="BB.png") and basilan==0):

            if self.basildimi:
                self.basildimi=False
            else:
                self.basildimi=True

        for i in board:

            if i.basildimi:
                if basilan==0:
                    basilan=basilan+1
                    basilan1id=i.id

                elif basilan==1:
                    basilan2id=i.id

                    for e in board:

                        for a in board:

                            if e.id==basilan1id and a.id==basilan2id:
                                if e.color==a.color:
                                    img1=e.img
                                    img2=a.img
                                    e.imagee=tk.PhotoImage(file=img1)
                                    a.imagee=tk.PhotoImage(file=img2)


                                else:
                                    if e.img[0]=="W":
                                        img3=e.img[1:]
                                        img4=a.img[1:]
                                        img3="B"+img3
                                        img4="W"+img4
                                        e.imagee=tk.PhotoImage(file=e.img)
                                        a.imagee=tk.PhotoImage(file=a.img)
                basilan=0












A8=square("B",1,1,i.BBR,"BBR")
A7=square("W",1,2,i.WBP,"WBP")
A6=square("B",1,3,i.BB,"free")
A5=square("W",1,4,i.WB,"free")
A4=square("B",1,5,i.BB,"free")
A3=square("W",1,6,i.WB,"free")
A2=square("B",1,7,i.BWP,"BWP")
A1=square("W",1,8,i.WWR,"WWR")

B8=square("W",2,1,i.WBK,"WBK")
B7=square("B",2,2,i.BBP,"BBP")
B6=square("W",2,3,i.WB,"free")
B5=square("B",2,4,i.BB,"free")
B4=square("W",2,5,i.WB,"free")
B3=square("B",2,6,i.BB,"free")
B2=square("W",2,7,i.WWP,"WWP")
B1=square("B",2,8,i.BWK,"BWK")

C8=square("B",3,1,i.BBB,"BBB")
C7=square("W",3,2,i.WBP,"WBP")
C6=square("B",3,3,i.BB,"free")
C5=square("W",3,4,i.WB,"free")
C4=square("B",3,5,i.BB,"free")
C3=square("W",3,6,i.WB,"free")
C2=square("B",3,7,i.BWP,"BWP")
C1=square("W",3,8,i.WWB,"WWB")

D8=square("W",4,1,i.WBQ,"WBQ")
D7=square("B",4,2,i.BBP,"BBP")
D6=square("W",4,3,i.WB,"free")
D5=square("B",4,4,i.BB,"free")
D4=square("W",4,5,i.WB,"free")
D3=square("B",4,6,i.BB,"free")
D2=square("W",4,7,i.WWP,"WWP")
D1=square("B",4,8,i.BWQ,"BWQ")

E8=square("B",5,1,i.BBXX,"BBXX")
E7=square("W",5,2,i.WBP,"WBP")
E6=square("B",5,3,i.BB,"free")
E5=square("W",5,4,i.WB,"free")
E4=square("B",5,5,i.BB,"free")
E3=square("W",5,6,i.WB,"free")
E2=square("B",5,7,i.BWP,"BWP")
E1=square("W",5,8,i.WWXX,"WWXX")

F8=square("W",6,1,i.WBB,"WBB")
F7=square("B",6,2,i.BBP,"BBP")
F6=square("W",6,3,i.WB,"free")
F5=square("B",6,4,i.BB,"free")
F4=square("W",6,5,i.WB,"free")
F3=square("B",6,6,i.BB,"free")
F2=square("W",6,7,i.WWP,"WWP")
F1=square("B",6,8,i.BWB,"BWB")

G8=square("B",7,1,i.BBK,"BBK")
G7=square("W",7,2,i.WBP,"WBP")
G6=square("B",7,3,i.BB,"free")
G5=square("W",7,4,i.WB,"free")
G4=square("B",7,5,i.BB,"free")
G3=square("W",7,6,i.WB,"free")
G2=square("B",7,7,i.BWP,"BWP")
G1=square("W",7,8,i.WWK,"WWK")

H8=square("W",8,1,i.WBR,"WBR")
H7=square("B",8,2,i.BBP,"BBP")
H6=square("W",8,3,i.WB,"H6")
H5=square("B",8,4,i.BB,"H5")
H4=square("W",8,5,i.WB,"H4")
H3=square("B",8,6,i.BB,"H3")
H2=square("W",8,7,i.WWP,"WWP")
H1=square("B",8,8,i.BWR,"BWR")



board=[A8,B8,C8,D8,E8,F8,G8,H8,
       A7,B7,C7,D7,E7,F7,G7,H7,
       A6,B6,C6,D6,E6,F6,G6,H6,
       A5,B5,C5,D5,E5,F5,G5,H5,
       A4,B4,C4,D4,E4,F4,G4,H4,
       A3,B3,C3,D3,E3,F3,G3,H3,
       A2,B2,C2,D2,E2,F2,G2,H2,
       A1,B1,C1,D1,E1,F1,G1,H1,]




















window.mainloop()
