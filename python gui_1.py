from tkinter import *
base = Tk()
base.geometry("500x450")
base.title("My app window")

frm=Frame(frm,bg="blue")
frm2.pack()
frm.pack(fill=BOTH,side=LEFT,expand=True)

dsp=label(frm,text="Enter Amount in Naira",fg="blue")
dsp.pack(ipady=10,ipadx==10,side=LEFT)

ent=Entry(frm,width=50)
ent.pack(expand=True,ipady=10,side=LEFT)

btn=Button(frm,fg)
lb.pack(ipady=10,ipadx==10,side=LEFT)
base.mainloop()
