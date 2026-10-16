from tkinter import *

FONT_NAME = "Times New Roman"

window = Tk()
window.title("Leave Booking")

# create the canvas
canvas = Canvas(width= 1000, height=1000)
canvas.grid(column=0, row=0)

#load and place the background image
front_img = PhotoImage(file="mountain_pic.png")
canvas.create_image(0, 0, image=front_img, anchor="nw")
canvas.create_text(400, 300, text="Welcome", fill= "white", font=(FONT_NAME, 35, "bold"))



# label

user_label =Label(text="Email/Username:")
user_label.grid(row= 2, column=0)
canvas.create_window(150, 400, window=user_label, width=200)

password_label = Label(text="Password:")
password_label.grid(row= 3, column=0)
canvas.create_window(150, 425, window=password_label, width=200)

# button
sign_in = Button(text="SIGN IN",width=36)
sign_in.grid(row=4, column=1)
canvas.create_window(400, 460, window=sign_in, width=200)


generate_password = Button(text="Forgot Password")
generate_password.grid(row=3 , column=2)
canvas.create_window(400, 500, window=generate_password, width=200)

# -------entry-----
user_entry = Entry(width=35)
user_entry.grid(row= 2, column=1, columnspan=2)
canvas.create_window(400, 400, window=user_entry, width=200)
user_entry.focus()

password_entry =Entry(width=21)
password_entry.grid(row= 3, column=1, columnspan=2)
canvas.create_window(400, 425, window=password_entry, width=200)


window.mainloop()