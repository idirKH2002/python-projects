from tkinter import * 
def show_password():
    password_label=Label(ma_fenetre, textvariable=password)
    password_label.grid(row=2 , column=2)
ma_fenetre= Tk()
password = StringVar()
password_entry = Entry(ma_fenetre,textvariable=password,show="*")
password_entry.grid(row=0, column=0)
show_password_button = Button(ma_fenetre, text="Dévoiler", command=show_password)
show_password_button.grid(row=1, column=1)
ma_fenetre.mainloop()