from tkinter import*
from tkinter.ttk import Combobox
class safal(Tk):
	def __init__(self):
		super().__init__()
		self.wet=StringVar()
		self.sql=DoubleVar()
		self.qwe=StringVar()
		
		self.config(bg="black")
		self.__as=Label(self,text="Currency",font="arial 15 bold underline",bg="black",fg="white").place(x=0)
		self.__asd=Label(self,text="Converter",font="arial 15 bold underline",bg="black",fg="white").place(x=290,y=0)
		self.ad=PhotoImage(file="vaik.png")
		self.qw=Label(self,image=self.ad,bg="black").place(x=200,y=60)
		self.__bn=Entry(self,textvariable=self.qwe,bd=7,width=85,borderwidth=14,relief=SUNKEN,bg="#51E1FC",fg="white",font="arial 12 bold")
		
		self.__bn.place(height=150,width=300,x=90,y=270)
		
class button(safal):
	def __init__(self):
		super().__init__()
		self.__x=PhotoImage(file="qw.png")
		self.__but=Button(self,image=self.__x,bd=7,bg="#51E1FC",command=self.safa)
		self.__but.place(x=5,y=503)
		self.__ent=Entry(self,bd=2,textvariable=self.sql,bg="red")
		self.__ent.place(width=160,height=50,x=0,y=445)
		self.ddd=Combobox(self,textvariable=self.wet,value=["usa","india","china","bangladesh","arab","singapore"]).place(height=50,x=173,y=445)
		self.__label=Label(self,text="",font="arial 8 bold underline")
		self.__label.place(x=0,y=700)
		self.__bu=Button(self,bitmap="info",command=self.sam)
		self.__bu.place(width=20,height=50,x=10,y=70)
		self.__cv=PhotoImage(file="op.png")
		self.__dd=Button(self,image=self.__cv,bd=7,bg="grey",command=self.quit)
		self.__dd.place(height=60,x=370,y=790)
		self.__er=Label(self,text="2020 copyright© safal",font=("arial 12 bold underline"),fg="white",bg="black")
		self.__er.place(x=0,y=815)
	def sam(self):
		self.__label.config(text="This is currencyconverter software by safal")
	def safa(self):
		self.ae=self.wet.get()
		self.al=self.sql.get()
		
		if self.ae=="usa":
			self.con=str(self.al*116)
			self.qwe.set(str("rupees is:")+self.con+str("RS"))
		elif self.ae=="india":
			self.con=str(self.al*0.63)
			self.qwe.set(str("rupees is:")+self.con+str("RS"))
		elif self.ae=="china":
			self.con=str(self.al*17.08)
			self.qwe.set(str("rupees is:")+self.con+str("RS"))
		elif self.ae=="bangladesh":
			self.con=str(self.al*1.43)
			self.qwe.set(str("rupees is:")+self.con+str("RS"))
		elif self.ae=="arab":
			self.con=str(self.al*32.92)
			self.qwe.set(str("rupees is:")+self.con+str("RS"))
		elif self.ae=="singapore":
			self.con=str(self.al*86.78)
			self.qwe.set(str("rupees is:")+self.con+str("RS"))
		elif self.ae=="pakistan":
			self.con=str(self.al*0.72)
			self.qwe.set(str("rupees is:")+self.con+str("RS"))
		elif self.ae=="japan":
			self.con=str(self.al*1.13)
			self.qwe.set(str("rupees is:")+self.con+str("RS"))
		else:
			self.qwe.set(str("oop try again"))
		
		
		
		
			
			
		
root=button()
if __name__=='__main__':
	root.mainloop()