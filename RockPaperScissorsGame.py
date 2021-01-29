from tkinter import *

rps = Tk()
rps.title("Rock Paper Scissors Game")
rps.geometry("800x500")
rps.maxsize(800,500)
rps.minsize(800,500)
player = "Archishman"
cs = Frame(rps, borderwidth = 1,padx=131,relief=FLAT,bg="white")
cs.pack(anchor=NW)
ps = Frame(rps, borderwidth = 1,padx=131,relief=FLAT,bg="white")
ps.pack(anchor=NE,side=TOP)
ps1 = Label(ps, text=f"{player}",font="Arial 20").pack()
cs1 = Label(cs, text="Computer",font="Arial 20").pack()
ps2 = Frame(rps, borderwidth = 5,bg="white",pady=213,padx=129,relief=FLAT)
ps2.pack(side=RIGHT,anchor=E)
cs2 = Frame(rps, borderwidth = 5,bg="white",pady=200,padx=120,relief=RIDGE)
cs2.pack(side=LEFT,anchor=W)
pst = Label(ps2, text="ScoreBoard").pack()
cst = Label(cs2, text="ScoreBoard").pack()


        

rps.mainloop()
