#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ---------------------------------------------------------------------------------------------
# Description:  Program to encrypt and decrypt text with a passphrase
# Author:       Fabien Ruf
# Date:         20.12.2019
# ---------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import scrolledtext as st
from tkinter import messagebox
from tkinter import filedialog

import random
import string

import crypting

# --------------- Functions ----------------
def randomStringDigits(stringLength):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def generatePassword():
    try:
        var=int(digits.get())
    except ValueError:
        messagebox.showinfo('Warning',"No Integer entered")
        return
    
    ky.delete(0, END)
    ky.insert(INSERT,randomStringDigits(var))
    check_show_psw.select()
    show_hide_psd()
    messagebox.showinfo('Warning',"Don't forget this password")


def on_encrypt_clicked():
    crypt(0)

def on_decrypt_clicked():
    crypt(1)

def crypt(p):
    text = txt.get(1.0, END).strip()
    key = ky.get().strip()
    
    outp.delete(1.0,END)

    if p == 0:
        res = crypting.encrypt(text,key) #calls function to encrypt
    else:
        res = crypting.decrypt(text,key) #calls function to encrypt

    if res == 'error':
        messagebox.showinfo('Warning', 'A character is invalid')
    else:
        outp.insert(INSERT,res)

def on_load_clicked():
    txt.delete(1.0,END) #maybe need deletation
    filename = filedialog.askopenfilename( initialdir="C:/", title="select file",
                                           filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    f = open(filename, "r")
    input= f.read()
    f.close()
    txt.insert(INSERT,input)

def on_save_clicked():
    f = filedialog.asksaveasfile(mode='w', title="Save the file",
            defaultextension=".txt", filetypes=(('all files', '.*'), ('text files', '.txt')),
                                 initialfile='cryptography_example')
    if f is None:
        return
    text2save = outp.get(1.0, END).strip()
    f.write(text2save)
    f.close()
    
    messagebox.showinfo('Save','The text has successfully been saved')

def show_hide_psd():
    if(check_var.get()):
        ky.config(show="")
    else:
        ky.config(show="*") 


# ----------------- GUI ------------------
style=("Arial Bold", 10)
h=40

window = Tk()

window.title("Cryptography tool")
window.geometry("470x505")


lbl = Label(window, text="Enter the text you want to encrypt or decrypt here: (or load it)", font=style)
lbl.place(x=20, y=10, height=h, width=360)
 
txt = st.ScrolledText(window)
txt.focus() 
txt.place(x=20,y=60, height=100, width=430)

outp = st.ScrolledText(window)
outp.place(x=20, y=325, height=100, width=430)

lbl2 = Label(window, text="Enter any password here:", font=style)
lbl2.place(x= 20, y=170, height=h)

check_var = IntVar()
check_show_psw = Checkbutton(window, text = "Show", variable = check_var, \
                 onvalue = 1, offvalue = 0,command = show_hide_psd)
check_show_psw.place(y=170,x=200, height=h)

digits = Entry(window,justify='center')
digits.insert(INSERT, 8 )
digits.place(x=340,y=180, height=20, width=20)

ky = Entry(window, show='*')
ky.place(x=20,y=220, height=25, width=415)

# ------------ Buttons --------------

btn0 = Button(window, text="Generate", command=generatePassword)
btn0.place(y=170,x=380, height=h, width=70)

btn1 = Button(window, text="ENCRYPT", command=on_encrypt_clicked)
btn1.place(y=265,x=20, height=h, width=70)
 
btn2 = Button(window, text="DECRYPT", command=on_decrypt_clicked)
btn2.place(y=265,x=150, height=h, width=70)


btn4 = Button(window, text="Save", command=on_save_clicked)
btn4.place(x=380,y=445,height=h, width=70)

btn5 = Button(window, text="Load", command=on_load_clicked)
btn5.place(x=20, y=445, height=h, width=70)

window.mainloop()
