import sys
from Tkinter import *
import MySQLdb
import tkMessageBox as msg







def start():
    tekst3=wpisek3.get()
    tekst2=wpisek2.get()
    tekst=wpisek.get()
    etykieta = Label(Gui, text=tekst).pack()
    etykieta2 = Label(Gui, text=tekst2).pack()
    dbc = MySQLdb.connect(host=tekst,user=tekst2, passwd=tekst3 )
    msg.INFO(db.rollback())

Gui=Tk()
wpisek=StringVar()
wpisek2=StringVar()
wpisek3=StringVar()


#label = Message( Gui, textvariable=var, relief=RAISED ).pack()
Gui.geometry ("555x120")
Gui.title('MySQL Conection tester')
nwpis= Label(Gui, text="Host").pack(side = LEFT)
wpis=Entry(Gui,  textvariable=wpisek, ).pack(side = LEFT)
wpis3=Entry(Gui, textvariable=wpisek3, show="*").pack(side = RIGHT)
nwpis3= Label(Gui, text="Passworld").pack(side = RIGHT)
wpis2=Entry(Gui, textvariable=wpisek2, ).pack(side = RIGHT)
nwpis2= Label(Gui, text="User").pack(side = RIGHT)


przycisk=Button(Gui, text="Testoj", command=start).pack(side = BOTTOM)



Gui.mainloop()