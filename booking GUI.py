from tkinter import *
from tkinter import ttk  # Added for the modern dropdown widget

# ---------------------------- UI SETUP ------------------------------- #
# constants
FONT_NAME = "Times New Roman"

window = Tk()
window.title("Leave Booking")

# create the canvas
canvas = Canvas(width= 1000, height=1000)
canvas.grid(column=0, row=0)

#load and place the background image
work_img = PhotoImage(file="workspace.png")
canvas.create_image(0, 0, image=work_img, anchor="nw")
canvas.create_text(200, 100, text="Out of Office", fill= "orange", font=(FONT_NAME, 30, "bold"))

# def submit_button:
    # .get() grabs whatever text is currently inside the inputs
    # leave_type = dropdown.get()
    # start_date = start_date_entry.get()
    # end_date = end_date_entry.get()
    # print(f"Booking: {leave_type} | From: {start_date} | To: {end_date}")


# ------------------Create the dropdown widget-----------------
#  Define your list of options
leave_options = ["Annual Leave", "Maternity/Paternity", "Unpaid Leave"]
dropdown = ttk.Combobox(window, values=leave_options, state="readonly", font=(FONT_NAME, 12))
dropdown.set("Select Leave Type")  # Default placeholder text

# (Adjust X and Y coordinates as needed)
canvas.create_window(400, 150, window=dropdown, width=200)

# -----------buttons-----------

submit = Button(text="Submit", font=(FONT_NAME, 12) )
canvas.create_window(400, 400, window=submit, width=200)


# ------------Labels--------------

# accrued label
accrued_leave = Label(text="Accrued Leave", font=(FONT_NAME, 12))
accrued_leave_count = Label(text="0", font=(FONT_NAME, 12))
canvas.create_window(200, 500, window=accrued_leave, width=150)
canvas.create_window(200, 450, window=accrued_leave_count, width=150)


# approved label
approved_leave = Label(text="Approved Leave", font=(FONT_NAME, 12))
approved_leave_count = Label(text="0", font=(FONT_NAME, 12))
canvas.create_window(500, 500, window=approved_leave, width=150)
canvas.create_window(500, 450, window=approved_leave_count, width=150)



# --------------------Start date input ------------------
# Adding anchor="w" to the label ensures it aligns perfectly to the left edge of the dropdown box.
canvas.create_text(130, 225, text="Start Date (DD/MM/YYYY):", fill="white", font=(FONT_NAME, 12, "bold"), anchor="w")
start_date_entry = ttk.Entry(window, style="Custom.TEntry")
canvas.create_window(230, 260, window=start_date_entry, width=200)

# -----------------------End date input-----------------
# Adding anchor="w" to the label ensures it aligns perfectly to the left edge of the dropdown box.
canvas.create_text(130, 300, text="End Date (DD/MM/YYYY):", fill="white", font=(FONT_NAME, 12, "bold"), anchor="w")
end_date_entry = ttk.Entry(window, style="Custom.TEntry")
canvas.create_window(230, 335, window=end_date_entry, width=200)

canvas.pack()



window.mainloop()