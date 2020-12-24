from tkinter import *
from tkinter import ttk
import random

def quit():
    window.destroy()




def getfrom():
    if lmb1var.get()=='Santragachi' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Santragachi')
        if lmb2var.get()=='Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost=str(30*psnumvar.get()-30*psnumvar1.get())
            Labelvar2.set(Tcost)

            x=random.randint(1096,9999)
            y=str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(20 * psnumvar.get() - 20 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(50 * psnumvar.get() - 50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(100 * psnumvar.get() - 100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(40 * psnumvar.get() - 40 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(70 * psnumvar.get() - 70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(10 * psnumvar.get() - 10 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(60 * psnumvar.get() - 60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

    elif lmb1var.get() == 'Kharagpur' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Kharagpur')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(30 * psnumvar.get() - 30 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(60 * psnumvar.get() - 60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(70 * psnumvar.get() - 70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(40 * psnumvar.get() - 40 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(50 * psnumvar.get() - 50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(100 * psnumvar.get() - 100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(20 * psnumvar.get() - 20 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(10 * psnumvar.get() - 10 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Sealdah' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Sealdah')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(20 * psnumvar.get() - 20 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(60 * psnumvar.get() - 60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(40 * psnumvar.get() - 40 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Malda':
            Labelvar1.set('Malda')
            Tcost = str(100 * psnumvar.get() - 100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(10 * psnumvar.get() - 10 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(30 * psnumvar.get() - 30 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Andul':
            Labelvar1.set('Andul')
            Tcost = str(50 * psnumvar.get() - 50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(80 * psnumvar.get() - 80 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

    elif lmb1var.get() == 'Burdwan' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Burdwan')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(50 * psnumvar.get() - 50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(40 * psnumvar.get() - 40 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(100 * psnumvar.get() - 100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Malda':
            Labelvar1.set('Malda')
            Tcost = str(70 * psnumvar.get() - 70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(60 * psnumvar.get() - 60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(30 * psnumvar.get() - 30 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Andul':
            Labelvar1.set('Andul')
            Tcost = str(50 * psnumvar.get() - 50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(90 * psnumvar.get() - 90 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

    elif lmb1var.get() == 'Malda' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Malda')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(100 * psnumvar.get() - 100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(70 * psnumvar.get() - 70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(70 * psnumvar.get() - 70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(60 * psnumvar.get() - 60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(90 * psnumvar.get() - 90 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Andul':
            Labelvar1.set('Andul')
            Tcost = str(80 * psnumvar.get() - 80 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

        elif lmb2var.get() == 'Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(50 * psnumvar.get() - 50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(100 * psnumvar.get() - 100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Dum Dum Junction' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Dum Dum Junction')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(40 * psnumvar.get() - 40 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(10 * psnumvar.get() - 10 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(60 * psnumvar.get() - 60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(60 * psnumvar.get() - 60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(30 * psnumvar.get() - 30 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(70 * psnumvar.get() - 70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(100 * psnumvar.get() - 100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(50 * psnumvar.get() - 50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)




    elif lmb1var.get() == 'Barasat' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Barasat')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(70 * psnumvar.get() - 70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(30 * psnumvar.get() - 30 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(30 * psnumvar.get() - 30 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(90 * psnumvar.get() - 90 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(30 * psnumvar.get() - 30 * psnumvar1.get())
            Labelvar2.set(Tcost)


            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(80 * psnumvar.get() - 80 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(60 * psnumvar.get() - 60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(100 * psnumvar.get() - 100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Andul' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Andul')
        if lmb2var.get()=='Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(20 * psnumvar.get() - 20 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(70 * psnumvar.get() - 70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(50 * psnumvar.get() - 50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(80 * psnumvar.get() - 80 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(70 * psnumvar.get() - 70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(60 * psnumvar.get() - 60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(100 * psnumvar.get() - 100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(10 * psnumvar.get() - 10 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Mednapur' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Mednapur')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(60 * psnumvar.get() - 60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(80 * psnumvar.get() - 80 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(90 * psnumvar.get() - 90 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(50 * psnumvar.get() - 50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(100 * psnumvar.get() - 100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(100 * psnumvar.get() - 100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(100 * psnumvar.get() - 100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(40 * psnumvar.get() - 40 * psnumvar1.get())
            Labelvar2.set(Tcost)


            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


    elif lmb1var.get()=='Santragachi' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Santragachi')
        if lmb2var.get()=='Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost=str(2*30*psnumvar.get()-2*30*psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*20 * psnumvar.get() - 2*20 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*50 * psnumvar.get() - 2*50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*100 * psnumvar.get() - 2*100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*40 * psnumvar.get() - 2*40 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*70 * psnumvar.get() - 2*70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*10 * psnumvar.get() - 2*10 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*60 * psnumvar.get() - 2*60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Kharagpur' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Kharagpur')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*30 * psnumvar.get() - 2*30 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*60 * psnumvar.get() - 2*60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*70 * psnumvar.get() - 2*70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*40 * psnumvar.get() - 2*40 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*50 * psnumvar.get() - 2*50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*100 * psnumvar.get() - 2*100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*20 * psnumvar.get() - 2*20 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*10 * psnumvar.get() - 2*10 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Sealdah' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Sealdah')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*20 * psnumvar.get() - 2*20 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*60 * psnumvar.get() - 2*60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*40 * psnumvar.get() - 2*40 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*100 * psnumvar.get() - 2*100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*10 * psnumvar.get() - 2*10 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*30 * psnumvar.get() - 2*30 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*50 * psnumvar.get() - 2*50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*80 * psnumvar.get() - 2*80 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

    elif lmb1var.get() == 'Burdwan' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Burdwan')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*50 * psnumvar.get() - 2*50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*40 * psnumvar.get() - 2*40 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*100 * psnumvar.get() - 2*100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*70 * psnumvar.get() - 2*70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*60 * psnumvar.get() - 2*60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*30 * psnumvar.get() - 2*30 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*50 * psnumvar.get() - 2*50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*90 * psnumvar.get() - 2*90 * psnumvar1.get())
            Labelvar2.set(Tcost)


            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)

    elif lmb1var.get() == 'Malda' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Malda')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*100 * psnumvar.get() - 2*100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*70 * psnumvar.get() - 2*70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*70 * psnumvar.get() - 2*70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*60 * psnumvar.get() - 2*60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*90 * psnumvar.get() - 2*90 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*80 * psnumvar.get() - 2*80 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*50 * psnumvar.get() - 2*50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(100 * psnumvar.get() - 100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Dum Dum Junction' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Dum Dum Junction')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*40 * psnumvar.get() - 2*40 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*10 * psnumvar.get() - 2*10 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*60 * psnumvar.get() - 2*60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*60 * psnumvar.get() - 2*60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*30 * psnumvar.get() - 2*30 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*70 * psnumvar.get() - 2*70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*100 * psnumvar.get() - 2*100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*50 * psnumvar.get() - 2*50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)




    elif lmb1var.get() == 'Barasat' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Barasat')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*70 * psnumvar.get() - 2*70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*30 * psnumvar.get() - 2*30 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*30 * psnumvar.get() - 2*30 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*90 * psnumvar.get() - 2*90 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*30 * psnumvar.get() - 2*30 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*80 * psnumvar.get() - 2*80 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*60 * psnumvar.get() - 2*60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*100 * psnumvar.get() - 2*100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Andul' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Andul')
        if lmb2var.get()=='Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*20 * psnumvar.get() - 2*20 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*70 * psnumvar.get() - 2*70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*50 * psnumvar.get() - 2*50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*80 * psnumvar.get() - 2*80 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*70 * psnumvar.get() - 2*70 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*60 * psnumvar.get() - 2*60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*100 * psnumvar.get() - 2*100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*10 * psnumvar.get() - 2*10 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Mednapur' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Mednapur')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*60 * psnumvar.get() - 2*60 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*80 * psnumvar.get() - 2*80 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*90 * psnumvar.get() - 2*90 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*50 * psnumvar.get() - 2*50 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*100 * psnumvar.get() - 2*100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*100 * psnumvar.get() - 2*100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*100 * psnumvar.get() - 2*100 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*40 * psnumvar.get() - 2*40 * psnumvar1.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)





    elif lmb1var.get()=='Santragachi' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Santragachi')
        if lmb2var.get()=='Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost=str(30*psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(20 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(40 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(10 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Kharagpur' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Kharagpur')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(40 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(20 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(10 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)





    elif lmb1var.get() == 'Sealdah' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Sealdah')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(20 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(40 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Malda':
            Labelvar1.set('Malda')
            Tcost = str(100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(10 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Andul':
            Labelvar1.set('Andul')
            Tcost = str(50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(80 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Burdwan' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Burdwan')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(40 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Malda':
            Labelvar1.set('Malda')
            Tcost = str(70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Andul':
            Labelvar1.set('Andul')
            Tcost = str(50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(90 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)




    elif lmb1var.get() == 'Malda' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Malda')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(90 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Andul':
            Labelvar1.set('Andul')
            Tcost = str(80 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Dum Dum Junction' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Dum Dum Junction')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(40 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(10 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)




    elif lmb1var.get() == 'Barasat' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Barasat')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(90 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(80 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Andul' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Andul')
        if lmb2var.get()=='Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(20 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(80 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(10 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Mednapur' and checkvar1.get()==1 and checkvar2.get()==0 and checkvar3.get()==1 and checkvar4.get()==1:
        Labelvar.set('Mednapur')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(80 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(90 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(40 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)





    elif lmb1var.get()=='Santragachi' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Santragachi')
        if lmb2var.get()=='Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost=str(2*30*psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*20 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*40 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*10 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Kharagpur' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Kharagpur')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*40 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*20 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*10 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)





    elif lmb1var.get() == 'Sealdah' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Sealdah')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*20 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*40 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*10 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*80 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Burdwan' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Burdwan')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*40 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*90 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Malda' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Malda')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*90 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*80 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Dum Dum Junction' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Dum Dum Junction')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*40 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*10 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)




    elif lmb1var.get() == 'Barasat' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Barasat')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*90 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*30 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*80 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Andul' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Andul')
        if lmb2var.get()=='Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*20 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*80 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*70 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Mednapur':
            Labelvar1.set('Mednapur')
            Tcost = str(2*100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*10 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)



    elif lmb1var.get() == 'Mednapur' and checkvar1.get()==0 and checkvar2.get()==1 and checkvar3.get()==1 and checkvar4.get()==0:
        Labelvar.set('Mednapur')
        if lmb2var.get() == 'Santragachi':
            Labelvar1.set('Santragachi')
            Tcost = str(2*60 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Sealdah':
            Labelvar1.set('Sealdah')
            Tcost = str(2*80 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Burdwan':
            Labelvar1.set('Burdwan')
            Tcost = str(2*90 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Malda':
            Labelvar1.set('Malda')
            Tcost = str(2*50 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Dum Dum Junction':
            Labelvar1.set('Dum Dum Junction')
            Tcost = str(2*100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Barasat':
            Labelvar1.set('Barasat')
            Tcost = str(2*100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get()=='Andul':
            Labelvar1.set('Andul')
            Tcost = str(2*100 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


        elif lmb2var.get() == 'Kharagpur':
            Labelvar1.set('Kharagpur')
            Tcost = str(2*40 * psnumvar.get())
            Labelvar2.set(Tcost)

            x = random.randint(1096, 9999)
            y = str(x)
            TrainVar.set(y)


def res():
    lmb1var.set("")
    lmb2var.set("")
    Labelvar.set("")
    Labelvar1.set("")
    Labelvar2.set("")
    psnumvar.set("0")
    psnumvar1.set("0")
    TrainVar.set("")
    checkvar1.set(0)
    checkvar2.set(0)
    checkvar3.set(0)
    checkvar4.set(0)






    


window=Tk()
window.geometry("1000x600")
window.title("Railway Management System")
Mainframe=Frame(window).pack(expand=True)



checkvar1=IntVar()
checkvar2=IntVar()
check1=Checkbutton(window, text="Single", variable=checkvar1, onvalue=1, offvalue=0, height=10, width=10).place(x=100,y=100)
check2=Checkbutton(window, text="Return", variable=checkvar2, onvalue=1, offvalue=0, height=10, width=10).place(x=12,y=100)



checkvar3=IntVar()
checkvar4=IntVar()
check3=Checkbutton(window, text="Adult", variable=checkvar3, onvalue=1, offvalue=0, height=10, width=10).place(x=100, y=12)
check4=Checkbutton(window, text="Child", variable=checkvar4, onvalue=1, offvalue=0, height=10, width=10).place(x=12, y=12)
labelc2=Label(window, text="Select Journey Type").place(x=50,y=130)
labelc1=Label(window, text="Select person").place(x=50,y=50)

button1=Button(window, text="Exit", bd=5, command=lambda:quit()).place(x=10,y=10)


lmb1=Label(window, text="Select From Destination").place(x=400,y=10)
lmb1var=StringVar()
lmb1var.set("")




destination_cmb=ttk.Combobox(window, textvariable=lmb1var, font=20)
destination_cmb['values']=('','Santragachi','Kharagpur','Sealdah','Burdwan','Malda','Dum Dum Junction','Barasat','Andul','Mednapur')
destination_cmb.current(0)
destination_cmb.place(x=350,y=50)


lmb2=Label(window, text="Select To Destination").place(x=400,y=100)
lmb2var=StringVar()
lmb2var.set("")


destination_cmb2=ttk.Combobox(window, textvariable=lmb2var, font=20)
destination_cmb2['values']=('','Santragachi','Kharagpur','Sealdah','Burdwan','Malda','Dum Dum Junction','Barasat','Andul','Mednapur')
destination_cmb2.current(0)
destination_cmb2.place(x=350,y=150)


button2=Button(window, text="Total", padx=50, pady=20, bd=5, command=lambda:getfrom()).place(x=350,y=200)

Labelvar=StringVar()
Labelvar.set("")

Labelvar1=StringVar()
Labelvar1.set("")


label1=Label(window, text="From", font=20).place(x=700,y=50)
l1text=Label(window, height=1, width=20, bd=5, relief="sunken", font=("arial",14,"bold"), textvariable=Labelvar).place(x=700,y=80)
label2=Label(window, text="To", font=20).place(x=700,y=120)
l2text=Label(window, height=1, width=20, bd=5, relief="sunken", font=("arial",14,"bold"), textvariable=Labelvar1).place(x=700,y=150)

Labelvar2=StringVar()
Labelvar2.set("")


label3=Label(window, text="Journey Cost", font=20).place(x=700,y=200)
l3text=Label(window, height=1, width=20, bd=5, relief="sunken",  font=("arial", 14, "bold"), textvariable=Labelvar2).place(x=700,y=230)

psnumvar=IntVar()
psnumvar.set("0")
label4=Label(window, text="Total Passenger Number", font=20).place(x=30,y=250)
psnum= Entry(window, width=20, bd=7, textvariable=psnumvar).place(x=30,y=300)


psnumvar1=IntVar()
psnumvar1.set("0")
label5=Label(window, text="Child Passenger Number", font=20).place(x=30,y=350)
psnum1= Entry(window, width=18, bd=7, textvariable=psnumvar1).place(x=30,y=400)


TrainVar=IntVar()
TrainVar.set("")

LabelTrain=Label(window,text="Train NO.", font=20).place(x=700,y=300)

TrainLabel=Label(window, relief="sunken", font=("arial",20, "bold"), textvariable=TrainVar, width=15).place(x=700, y=350)


reset=Button(window, text="Reset", padx=30, pady=10, bd=10, command=lambda:res()).place(x=500, y=400)

window.mainloop()
