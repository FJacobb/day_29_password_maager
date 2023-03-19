from tkinter import Tk, PhotoImage,Canvas,Button, Entry, messagebox
from passwod import PassGenerate
FONT = ("Share Tech Mono", 7)
def generate_password():
    password.delete(0,"end")
    password.insert(0,pas.computer_selection())

def save_recode():
    if website.get() == "" and email.get() == "" and password.get() == "":
        messagebox.showerror("Error", "Yow have an empty field,\n please make sure you complete the field")
    else:
        with open("data/.password.txt", mode="a") as file:
            file.write(f"{website.get()}    |    {email.get()}    |    {password.get()}\n")



home = Tk()
pas = PassGenerate()
background = PhotoImage(file="image/Asset 8ldpi.png")

genete = PhotoImage(file="image/GENRATEldpi.png")
add = PhotoImage(file="image/addldpi.png")
home.geometry("426x266")
home.title("Password Manager")
canver = Canvas(width=428, height=268)
canver.create_image(214.,134, image=background)
website = Entry(width=27, bg="white", font=FONT, border=0)
website.place(x=62,y=107)
email = Entry(width=23, bg="white", font=FONT, border=0)
email.place(x=85,y=133)
password = Entry(width=12, bg="white", font=FONT, border=0)
password.place(x=62,y=158)
gnt = Button(image=genete, border=0, bg="#2c93cb", command=generate_password)
gnt.place(x=129, y=153)
add_button = Button(image=add, border=0, bg="#2c93cb", command=save_recode)
add_button.place(x=80, y=180)
canver.place(x=-2, y=-1)
home.mainloop()