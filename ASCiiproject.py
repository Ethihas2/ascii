from tkinter import *

root = Tk()
root.title("ASCII")
root.geometry("400x400")
root.configure(background="steelblue1")

input_var = Entry(root)
input_var.place(relx=0.5, rely=0.4, anchor=CENTER)
label_ascii = Label(root,text="Name in ASCII: ",bg="DarkSeaGreen1",fg="black")
label_encrypt = Label(root,text="Name Encrypted: ",bg="DarkSeaGreen1",fg="black")

def encrypt():
    label_ascii["text"]="Name in ASCII: "
    label_encrypt["text"]="Name Encrypted: "
    input_value = input_var.get()
    for letter in input_value:
        label_ascii["text"]+=str(ord(letter))+ " "
        label_encrypt["text"]+=str(chr(int(ord(letter)-1)))

button1 = Button(root,text="Show name in ASCII",command=encrypt,bg="red",fg="gray")
button1.place(relx=0.5,rely=0.5,anchor=CENTER)
label_ascii.place(relx=0.5,rely=0.6,anchor=CENTER)
label_encrypt.place(relx=0.5,rely=0.7,anchor=CENTER)


root.mainloop()