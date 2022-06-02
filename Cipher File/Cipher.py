# SOURCE CODE

# File Path - C:\Users\varvi\TextFiles\Assignments\My_Project_1\Final_Project.py

import pickle
import pandas as pd
import pyperclip
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

# 22 functions

# Encodes and Decodes the text in Atbash Script
def Atbash_encode_decode(code):
    message=''
    
    for i in code:
            if i.isalpha()==False:
                message+=i
            else:
                if ord(i)<91:    
                    b = ord(i)
                    c = 91-b
                    d = 64 + c
                    message+=chr(d)
                else:
                    b = ord(i)
                    c= 123-b
                    d = 96 + c
                    message+=chr(d)
    
    return message

# Encodes the text in Caesar Script
def caesar_shift_encoder(code,ind1,ind2):
    message=''

    for i in code:
        if i.isupper():
            b=ord(i)+ind1
            if b>90:
                c=64+(b-90)
                message+=chr(c)
            else:
                c=b
                message+=chr(c)
        elif i.islower():
            b=ord(i)+ind2
            if b>122:
                c=96+(b-122)
                message+=chr(c)
            else:
                c=b
                message+=chr(c)
        else:
            message+=i

    return message

# Encodes the text in Vigenere Script
def vigenere_encoder(code, key):
    message = ""
    
    small_alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    letter_to_index_s = dict(zip(small_alphabet, range(len(small_alphabet))))
    index_to_letter_s = dict(zip(range(len(small_alphabet)), small_alphabet))
    
    big_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    letter_to_index_b = dict(zip(big_alphabet, range(len(big_alphabet))))
    index_to_letter_b = dict(zip(range(len(big_alphabet)), big_alphabet))
    
    temp_code1 = ''
    split_code = []
    
    for i in code:
        if i.isalpha():
            temp_code1+=i
 
    for p in range(0,len(temp_code1),len(key)):
        split_code.append(temp_code1[p : p+len(key)])
        
    for each_split in split_code:
        i = 0
        for letter in each_split:
                if letter.islower():
                    number = (letter_to_index_s[letter] + letter_to_index_s[key[i].lower()]) % len(small_alphabet)
                    message += index_to_letter_s[number]
                    
                elif letter.isupper():
                    number = (letter_to_index_b[letter] + letter_to_index_b[key[i].upper()]) % len(big_alphabet)
                    message += index_to_letter_b[number]
                    
                i += 1
    
    mode_list = []
    
    for i in message:
        mode_list.append(i) 
    
    
    for i in range(len(code)):
        if code[i].isalpha():
            pass
        else:
            mode_list.insert(i,code[i])    
        
    message = ''
    
    for k in mode_list:
        message+=k
        
    return message

# Decodes the text in Caesar Script
def caesar_shift_decoder(code,ind1,ind2):
    message=''

    for i in code:
        if i.isupper():
            b=ord(i)-ind1
            if b<65:
                c=91-(65-b)
                message+=chr(c)
            else:
                c=b
                message+=chr(c)
        elif i.islower():
            b=ord(i)-ind2
            if b<97:
                c=123-(97-b)
                message+=chr(c)
            else:
                c=b
                message+=chr(c)
        else:
            message+=i

    return message

# Decodes the text in Vigenere Script
def vigenere_decoder(code, key):
    message = ""
    
    small_alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    letter_to_index_s = dict(zip(small_alphabet, range(len(small_alphabet))))
    index_to_letter_s = dict(zip(range(len(small_alphabet)), small_alphabet))
    
    big_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    letter_to_index_b = dict(zip(big_alphabet, range(len(big_alphabet))))
    index_to_letter_b = dict(zip(range(len(big_alphabet)), big_alphabet))
    
    temp_code1 = ''
    split_code = []
    
    for i in code:
        if i.isalpha():
            temp_code1+=i
 
    for p in range(0,len(temp_code1),len(key)):
        split_code.append(temp_code1[p : p+len(key)])
        
    for each_split in split_code:
        i = 0
        for letter in each_split:
                if letter.islower():
                    number = (letter_to_index_s[letter] - letter_to_index_s[key[i].lower()]) % len(small_alphabet)
                    message += index_to_letter_s[number]
                    
                elif letter.isupper():
                    number = (letter_to_index_b[letter] - letter_to_index_b[key[i].upper()]) % len(big_alphabet)
                    message += index_to_letter_b[number]
                    
                i += 1
    
    mode_list = []
    
    for i in message:
        mode_list.append(i) 
    
    for i in range(len(code)):
        if code[i].isalpha():
            pass
        else:
            mode_list.insert(i,code[i])    
        
    message = ''
    
    for k in mode_list:
        message+=k
        
    return message

# Reads the txt file
def text_file(file):
    fileobj = open(file,'r')
    reader= fileobj.readlines
    lines=''
    
    for i in reader():
        lines+=i
    
    fileobj.close()
    return lines

# Reads the dat file
def binary_file(file):
    try:
        fileobj = open(file,'rb')
        content1 = pickle.load(fileobj)
        fileobj.close()
        
        return content1
    
    except:
        message = messagebox.showerror('Unpickling error','The data was truncated')

# Reads the csv file
def csv_file(file):
    reader = pd.read_csv(file)
    list1 = []
    list2 = []
    
    for j in range(len(reader)):
        for i in range(len(reader.columns.values)):
            content1 = reader.iloc[j,i]
            list1.append(content1) 
        list2.append(list1)
        list1=[]
    
    df1 = pd.DataFrame(list2,columns=reader.columns.values)
    
    return df1.to_string(index=False)

# Sends the text and other requirements to the following scripts for encoding
def encode_sender(encode,code,ind1='none',ind2='none',primary_key='none'):
    if encode==1:
        text = Atbash_encode_decode(code)
    elif encode==2:    
        text = caesar_shift_encoder(code,ind1,ind2)
    elif encode==3:
        text = vigenere_encoder(code, primary_key)
    else:
        message = messagebox.showerror('Error','Please try again')
    
    return text

# Sends the text and other requirements to the following scripts for decoding
def decode_sender(decode,code,ind1='none',ind2='none',primary_key='none'):
    if decode==1:
        text = Atbash_encode_decode(code)
    elif decode==2:
        text = caesar_shift_decoder(code,ind1,ind2)
    elif decode==3:
        text = vigenere_decoder(code, primary_key)
    else:
        message = messagebox.showerror('Error','Please try again')
    
    return text

# Writes the contents to the txt file
def write_txt(file_name,mod):
    try:
        fobj1 = open(file_name,'w')
        fobj1.writelines(mod)
        fobj1.close()
    except:
        message = messagebox.showerror('Error','Please try again')

# Writes the contents to the dat file
def write_dat(file_name,mod):
    try:
        fobj1 = open(file_name,'wb')
        pickle.dump(mod,fobj1)
        fobj1.close()
    except:
        message = messagebox.showerror('Error','Please try again')

#------------------------------------------------------------------------------

# Opens the file dialog box in Cipher section
def fileselector_for_cipher():
    content=''
    
    try:
        l = (('txt files','*.txt'),('dat files','*.dat'),('csv files','*.csv'))
        filename = filedialog.askopenfilename(initialdir='C',title='Select a file',filetypes=l)
        if filename[-3:]=='txt':
            content = text_file(filename)
        elif filename[-3:]=='dat':
            content = binary_file(filename)
        elif filename[-3:]=='csv':
            content = csv_file(filename)
            
        t1.insert(tk.END,content)

    except:
        pass

# Enables and Disables the parameters depending on the cipher selected
def params(event):
    ind1_entry.delete(0,END)
    ind2_entry.delete(0,END)
    primary_key_entry.delete(0,END)
    
    if encode_type.get()=='Atbash':
        ind1_entry['state']=DISABLED
        ind2_entry['state']=DISABLED
        primary_key_entry['state']=DISABLED
            
    elif encode_type.get()=='Caesar Cipher':
        ind1_entry['state']=NORMAL
        ind2_entry['state']=NORMAL
        primary_key_entry['state']=DISABLED
        
    elif encode_type.get()=='Vigenere Cipher':
        ind1_entry['state']=DISABLED
        ind2_entry['state']=DISABLED
        primary_key_entry['state']=NORMAL

# Runs the operation after the convert button is pressed
def convert_pressed():
    code=t1.get('1.0',END)
    answer=''
    abc = True
    
    t2['state'] = NORMAL
    
    # Operation ENCODE
    if operation_type.get()=='Encode':
        # Encode Albash
        if encode_type.get()=='Atbash':
            encode=1
            answer=encode_sender(encode, code)
            
        # Encode Caesar Cipher
        elif encode_type.get()=='Caesar Cipher':
            var=False
            
            if ind1_entry.get().isdigit() and ind2_entry.get().isdigit():
                var=True
            else:
                message = messagebox.showerror('Valuen Error','Please enter an integer')
                abc = False
                
            if var==True:
                if int(ind1_entry.get())<26 and int(ind2_entry.get())<26:
                    encode=2
                    answer=encode_sender(encode, code, int(ind1_entry.get()),int(ind2_entry.get()))
                else:
                    message = messagebox.showwarning('Integer above 25','Please enter an integer less than 25.')
                    abc = False
            
            
        # Encode Vigenere Cipher
        elif encode_type.get()=='Vigenere Cipher':
            try:
                var=False
                for samp in primary_key_entry.get():
                    if samp.isdigit() or samp.isspace():
                        var=True
                        
                if var==False:
                    encode=3
                    answer=encode_sender(encode,code,ind1='',ind2='',primary_key=primary_key_entry.get())
                else:
                    message = messagebox.showerror('Error','Please enter a complete string without spaces')
                    abc = False
                    
            except ZeroDivisionError:
                message = messagebox.showerror('Error','Please enter a primary key')
                abc = False
        else:
            
            message = messagebox.showwarning('Encoder not selected','Encoding type not selected')
            abc = False
    
    # Operation DECODE
    elif operation_type.get()=='Decode':
        # Decode Atbash
        if encode_type.get()=='Atbash':
            decode=1
            answer=decode_sender(decode, code)            
        
        # Decode Caesar Cipher
        elif encode_type.get()=='Caesar Cipher':
            var=False
            
            if ind1_entry.get().isdigit() and ind2_entry.get().isdigit():
                var=True
            else:
                message = messagebox.showerror('Value Error','Please enter an integer')
                abc = False
            
            
            if var==True:
                if int(ind1_entry.get())<26 and int(ind2_entry.get())<26:
                    decode=2
                    answer=decode_sender(decode, code, int(ind1_entry.get()),int(ind2_entry.get()))
                else:
                    message = messagebox.showwarning('Integer above 25','Please enter an integer less than 25.')
                    abc = False
        
        # Decode Vigenere Cipher
        elif encode_type.get()=='Vigenere Cipher':
            try:
                var=False
                for samp in primary_key_entry.get():
                    if samp.isdigit() or samp.isspace():
                        var=True
                        
                if var==False:
                    decode=3
                    answer=decode_sender(decode,code,ind1='',ind2='',primary_key=primary_key_entry.get())
                else:
                    message = messagebox.showerror('Error','Please enter a complete string without spaces')
                    abc = False
                    
            except ZeroDivisionError:
                message = messagebox.showerror('Error','Please enter a primary key')
                abc = False
                
        else:
            
            message = messagebox.showwarning('Decoder not selected','Decoding type not selected')
            abc = False
    else:
        
        message = messagebox.showwarning('Operation not selected','Please select operation')
        abc = False
    
    t2.insert(tk.END,answer)
    t2['state'] = DISABLED

# Clears the contents inside the textbox in Cipher Section
def clear():
    t1.delete('1.0',END)
    
    t2['state'] = NORMAL
    t2.delete('1.0',END)
    t2['state'] = DISABLED

# Raises the frame
def raiseframe(frame):
    frame.tkraise()
    clear()
    simp_clear()

# Copies the text in the right textbox to the clip board
def copy_button_cipher():
    t2['state'] = NORMAL
    pyperclip.copy(t2.get('1.0',END))
    t2['state'] = DISABLED

# -----------------------------------------------------------------------------

# Opens the file dialog box in Simple File Handler section
def file_selector_simple():
    content=''
    
    try:
        l = (('txt files','*.txt'),('dat files','*.dat'),('csv files','*.csv'))
        filename2 = filedialog.askopenfilename(initialdir='C',title='Select a file',filetypes=l)
        
        if filename2[-3:]=='txt':
            content = text_file(filename2)
        
        elif filename2[-3:]=='dat':
            content = binary_file(filename2)
        
        elif filename2[-3:]=='csv':
            content = csv_file(filename2)
            
        text_here.insert(INSERT,content)
    
    except:
        pass

# Clears the text in Simple File Handler
def simp_clear():
    text_here.delete('1.0',END)

# Saves the contents in the textbox to a file
def file_saver(tbox):
    file_save_name = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    file_here = str(file_save_name)
    
    t2['state'] = NORMAL
    
    try:
        q = file_here.split('=')
        fin_name = q[1][1:-6]
        
        if fin_name[-3:]=='txt':
            write_txt(fin_name,tbox.get('1.0',END))
        elif fin_name[-3:]=='dat':
            write_dat(fin_name,tbox.get('1.0',END))
        elif fin_name[-3:]=='csv':
            write_csv(tbox,fin_name)
        else:
            message = messagebox.showerror('Error','File type not supported.')
        
    except IndexError:
        pass
    
    try:
        file_save_name.close()
    
    except AttributeError:
        pass

    t2['state'] = DISABLED

# Writes the contents to the csv file
def write_csv(tbox,fin_name):
    try:
        cols = tbox.get('1.0','2.0')
        cont = tbox.get('2.0',END)
        
        cols_mod = cols.split()
        cont_mod = cont.split()
        l1 = []
        l2 = []
        
        for i in range(0,len(cont_mod),len(cols_mod)):
            l1 = cont_mod[i:i+len(cols_mod)]
            l2.append(l1)
        
        dff = pd.DataFrame(l2,columns=cols_mod)
        dff.to_csv(fin_name,index=False)
        
        message = messagebox.showinfo('Success','The file was saved!')
        
    except:
        message = messagebox.showerror('Error','Something went wrong')

#------------------------------------------------------------------------------

# remember 580, 325
root = Tk()
m = root.maxsize()
g = str(m[0])+'x'+str(m[1])
root.geometry(g)
root.configure(bg='black')
root.title('Crypton')

# Home Screen 
fhome = Frame(root,width=1600,height=200,bg='black')
fhome.pack()
fhome.place(x=0, y=0, width=m[0], height=m[1])

desc1 = 'Welcome to Crypton. Please select the desired operation.'

home_entry_label = Label(fhome,text=desc1,font=('Heveletica',15),
                         bg='white',fg='black',padx=20,pady=8)

home_entry_label.pack(padx=20,pady=20)

to_f1_button = Button(fhome,text='Encrypt/Decrypt Text',command=lambda: raiseframe(f1),
                     width=20,height=1,font=('Heveletica',13),bg='lime',borderwidth=10)

to_f1_button.pack(padx=20,pady=20)

to_f2_button = Button(fhome,text='Simple File Handler',command=lambda: raiseframe(f2),
                     width=20,height=1,font=('Heveletica',13),bg='lime',borderwidth=10)

to_f2_button.pack(padx=20,pady=20)

help_button = Button(fhome,text='Help',width=20,height=1,command=lambda: raiseframe(f3),
                     font=('Heveletica',13),bg='lime',borderwidth=10)

help_button.pack(padx=20,pady=20)

desc2 = '*****Click on help and read the documentation before using the program*****'

home_entry_label_2 = Label(fhome,text=desc2,font=('Heveletica',15),
                         bg='white',fg='red',padx=20,pady=8)

home_entry_label_2.pack(padx=20,pady=20)

# -----------------------------------------------------------------------------

# Cipher Is Over Here
f1 = Frame(root,width=1600,height=200,bg='black')
f1.pack()
f1.place(x=0, y=0, width=m[0], height=m[1])

# For the file button
file_button = Button(f1,text='Select File',command=fileselector_for_cipher,borderwidth=8,
                     width=20,height=2,font=('Heveletica',13),bg='white')
file_button.grid(padx=20,pady=20,row=0,column=0)

# For the drop down menu for operation type
operation_type = StringVar()
operations = ['Encode','Decode']

operation_type.set('Select the operation')

dropdown_menu1 = OptionMenu(f1,operation_type, *operations)
dropdown_menu1.config(width=25,bg='red',height=2,fg='white',font=('Heveletica',13))
dropdown_menu1.grid(row=0,column=1,padx=10,pady=20)

# For the drop down menu for encode type
encode_type = StringVar()
encrypters = ['Atbash','Caesar Cipher','Vigenere Cipher']

encode_type.set('Select the script')

dropdown_menu2 = OptionMenu(f1,encode_type, *encrypters,command=params)
dropdown_menu2.config(width=25,bg='red',height=2,fg='white',font=('Heveletica',13))
dropdown_menu2.grid(row=0,column=2,padx=20,pady=20)

# For the back button
back_button = Button(f1,text='Back',width=20,height=2,command=lambda: raiseframe(fhome),
                     font=('Heveletica',13),bg='white',borderwidth=8)

back_button.grid(row=0,column=3,padx=20,pady=20)

# Index 1 label, entry and button
ind1_label = Label(f1,text='Enter index for small letters(Caesar Cipher)-',
                   font=('Heveletica',13),bg='purple',fg='white',padx=20,pady=8)

ind1_label.grid(row=1,column=0,padx=50,pady=10)

ind1_entry = Entry(f1,width=5,state=DISABLED,borderwidth=5)
ind1_entry.grid(row=1,column=1,sticky='w',padx=50)

# Index 2 label, entry and button
ind2_label = Label(f1,text='Enter index for capital letters(Caesar Cipher)-',
                   font=('Heveletica',13),bg='purple',fg='white',padx=20,pady=8)

ind2_label.grid(row=2,column=0,padx=50,pady=30)

ind2_entry = Entry(f1,width=5,state=DISABLED,borderwidth=5)
ind2_entry.grid(row=2,column=1,sticky='w',padx=50)

# Primary Key label, entry and button
primary_key_label = Label(f1,text='Enter the primary key(Vigenere Cipher)-',
                          font=('Heveletica',13),bg='purple',fg='white',padx=20,pady=7)

primary_key_label.grid(row=1,column=2,rowspan=2,padx=20)

primary_key_entry = Entry(f1,width=35,state=DISABLED,borderwidth=5)
primary_key_entry.grid(row=1,column=3,rowspan=2)

# Text column 1
xscrollbar1 = Scrollbar(f1,orient=HORIZONTAL)
xscrollbar1.grid(row=4,column=0,padx=50,columnspan=2,sticky='ew')

t1 = scrolledtext.ScrolledText(f1,wrap=NONE,xscrollcommand=xscrollbar1.set)
t1.grid(row=3,column=0,padx=50,columnspan=2,sticky='we')

xscrollbar1.config(command=t1.xview)

# Text column 2
xscrollbar2 = Scrollbar(f1,orient=HORIZONTAL)
xscrollbar2.grid(row=4,column=2,padx=50,columnspan=2,sticky='ew')

t2 = scrolledtext.ScrolledText(f1,wrap=NONE,xscrollcommand=xscrollbar2.set)
t2.grid(row=3,column=2,padx=50,columnspan=2,sticky='we')

xscrollbar2.config(command=t2.xview)
t2['state'] = DISABLED

# Clear Button
clear_button = Button(f1,text='Clear',width=13,command=clear,pady=8,
                      bg='orange',fg='black',font=('Heveletica',13))

clear_button.grid(row=5,column=0,padx=30,pady=50)

# Copy Button
copy_button = Button(f1,text='Copy',width=13,command=copy_button_cipher,pady=8,
                      bg='orange',fg='black',font=('Heveletica',13))

copy_button.grid(row=5,column=2,sticky='e',padx=30,pady=50)

# Convert Button
convert_button = Button(f1,text='Convert',width=10,command=convert_pressed,
                        bg='blue',fg='white',font=('Heveletica',13),padx=20,pady=8)

convert_button.grid(row=5,column=1,sticky='w',columnspan=2,padx=40,pady=50)

# Save Button
save_button_cipher = Button(f1,text='Save',width=13,command=lambda: file_saver(t2),pady=8,
                            bg='orange',fg='black',font=('Heveletica',13))

save_button_cipher.grid(row=5,column=3,columnspan=2,padx=30,pady=50)

# -----------------------------------------------------------------------------

# Simple File Handler
f2 = Frame(root,width=1600,height=200,bg='black')
f2.pack()
f2.place(x=0, y=0, width=m[0], height=m[1])

# --------------------------------------------------

back_button = Button(f2,text='Back',width=20,height=2,command=lambda: raiseframe(fhome),
                     font=('Heveletica',13),bg='white',borderwidth=8)

back_button.grid(row=0,column=0,padx=20,pady=20)

# --------------------------------------------------

xscrollbar2_here = Scrollbar(f2,orient=HORIZONTAL)
xscrollbar2_here.grid(row=2,column=1,padx=50,columnspan=2,sticky='ew')

text_here = scrolledtext.ScrolledText(f2,wrap=NONE,width=120,height=35,xscrollcommand=xscrollbar2_here.set)
text_here.grid(row=1,column=1,columnspan=2,padx=50)

xscrollbar2_here.config(command=text_here.xview)
# --------------------------------------------------

file_button_f2 = Button(f2,text='Select File',command=file_selector_simple,borderwidth=8,
                        width=20,height=2,font=('Heveletica',13),bg='white')

file_button_f2.grid(padx=20,pady=20,row=0,column=1)

# --------------------------------------------------

clear_button_simp = Button(f2,text='Clear',width=13,command=simp_clear,pady=8,
                           bg='orange',fg='black',font=('Heveletica',13))

clear_button_simp.grid(row=3,column=1,padx=30,pady=50)

# --------------------------------------------------

save_button_simp = Button(f2,text='Save',width=13,command=lambda: file_saver(text_here),pady=8,
                          bg='orange',fg='black',font=('Heveletica',13))

save_button_simp.grid(row=3,column=2,padx=30,pady=50)

# -----------------------------------------------------------------------------

f3 = Frame(root,width=1600,height=200,bg='black')
f3.pack()
f3.place(x=0, y=0, width=m[0], height=m[1])

back_button = Button(f3,text='Back',width=20,height=2,command=lambda: raiseframe(fhome),
                     font=('Heveletica',13),bg='white',borderwidth=8)

back_button.grid(row=0,column=0,padx=20,pady=20)

file__1 = open('help.txt','r')
all_needed = file__1.read()

xscrollbar2_help = Scrollbar(f3,orient=HORIZONTAL)
xscrollbar2_help.grid(row=2,column=1,padx=50,sticky='ew')

text_help = scrolledtext.ScrolledText(f3,wrap=NONE,width=125,height=35,xscrollcommand=xscrollbar2_help.set)
text_help.grid(row=1,column=1,padx=50)

xscrollbar2_help.config(command=text_help.xview)

text_help.insert('1.0',all_needed)
text_help['state'] = DISABLED

# -----------------------------------------------------------------------------
fhome.tkraise()
root.mainloop()
#------------------------------------------------------------------------------

