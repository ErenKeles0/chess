import tkinter as tk
import images as i


window=tk.Tk()
window.title("Chess")
window.geometry("576x576")
window.resizable(width=False, height=False)



basilan=0

class square():
    def __init__(self,color,rotateX,rotateY,images,id):
        self.id=id
        self.color=color
        self.basildimi=False
        self.rotatex=(rotateX*72)-72
        self.rotatey=(rotateY*72)-72
        self.img=images
        self.imagee=tk.PhotoImage(file=images)
        self.button=tk.Button(image=self.imagee,command=self.basildi1)
        self.button.place(width=72,height=72,x=self.rotatex,y=self.rotatey)

    def basildi1(self):
        global basilan1id
        global basilan1color
        global basilan1img
        global basilan

        if basilan==0:

            basilan=basilan+1
            basilan1id=self.id
            basilan1color=self.color
            basilan1img=self.img


        elif basilan==1:
            if not self.id[1]==basilan1id[1]:
                for i in board:
                    if i.id==basilan1id:

                        img1=i.imagee
                        img2=self.imagee
                        self.button["image"]=img1
                        i.button["image"]=img2


            basilan=0










A8=square("B",1,1,i.BBR,"BBR")
A7=square("W",1,2,i.WBP,"WBP1")
A6=square("B",1,3,i.BB,"free1")
A5=square("W",1,4,i.WB,"free2")
A4=square("B",1,5,i.BB,"free3")
A3=square("W",1,6,i.WB,"free4")
A2=square("B",1,7,i.BWP,"BWP1")
A1=square("W",1,8,i.WWR,"WWR")

B8=square("W",2,1,i.WBK,"WBK")
B7=square("B",2,2,i.BBP,"BBP1")
B6=square("W",2,3,i.WB,"free5")
B5=square("B",2,4,i.BB,"free6")
B4=square("W",2,5,i.WB,"free7")
B3=square("B",2,6,i.BB,"free8")
B2=square("W",2,7,i.WWP,"WWP1")
B1=square("B",2,8,i.BWK,"BWK")

C8=square("B",3,1,i.BBB,"BBB")
C7=square("W",3,2,i.WBP,"WBP2")
C6=square("B",3,3,i.BB,"free9")
C5=square("W",3,4,i.WB,"free10")
C4=square("B",3,5,i.BB,"free11")
C3=square("W",3,6,i.WB,"free12")
C2=square("B",3,7,i.BWP,"BWP2")
C1=square("W",3,8,i.WWB,"WWB")

D8=square("W",4,1,i.WBQ,"WBQ")
D7=square("B",4,2,i.BBP,"BBP2")
D6=square("W",4,3,i.WB,"free13")
D5=square("B",4,4,i.BB,"free14")
D4=square("W",4,5,i.WB,"free15")
D3=square("B",4,6,i.BB,"free16")
D2=square("W",4,7,i.WWP,"WWP2")
D1=square("B",4,8,i.BWQ,"BWQ")

E8=square("B",5,1,i.BBXX,"BBXX")
E7=square("W",5,2,i.WBP,"WBP3")
E6=square("B",5,3,i.BB,"free17")
E5=square("W",5,4,i.WB,"free18")
E4=square("B",5,5,i.BB,"free19")
E3=square("W",5,6,i.WB,"free20")
E2=square("B",5,7,i.BWP,"BWP3")
E1=square("W",5,8,i.WWXX,"WWXX")

F8=square("W",6,1,i.WBB,"WBB")
F7=square("B",6,2,i.BBP,"BBP3")
F6=square("W",6,3,i.WB,"free21")
F5=square("B",6,4,i.BB,"free22")
F4=square("W",6,5,i.WB,"free23")
F3=square("B",6,6,i.BB,"free24")
F2=square("W",6,7,i.WWP,"WWP3")
F1=square("B",6,8,i.BWB,"BWB")

G8=square("B",7,1,i.BBK,"BBK")
G7=square("W",7,2,i.WBP,"WBP4")
G6=square("B",7,3,i.BB,"free25")
G5=square("W",7,4,i.WB,"free26")
G4=square("B",7,5,i.BB,"free27")
G3=square("W",7,6,i.WB,"free28")
G2=square("B",7,7,i.BWP,"BWP4")
G1=square("W",7,8,i.WWK,"WWK")

H8=square("W",8,1,i.WBR,"WBR")
H7=square("B",8,2,i.BBP,"BBP4")
H6=square("W",8,3,i.WB,"free29")
H5=square("B",8,4,i.BB,"free30")
H4=square("W",8,5,i.WB,"free31")
H3=square("B",8,6,i.BB,"free32")
H2=square("W",8,7,i.WWP,"WWP4")
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
