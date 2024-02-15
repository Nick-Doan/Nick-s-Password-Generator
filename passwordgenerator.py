import random
import string
import customtkinter

# Password generator
def generate_password(length):
    total = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(total, length))
    return password

# Appearance
customtkinter.set_appearance_mode("System")

# GUI
app = customtkinter.CTk()
app.geometry("600x500")
app.title("Nick's Password Generator")

# Function to generate password and update textbox
def generate_password_and_update():
    length = int(optionmenu.get())  # Get the selected length from the dropdown
    generated_password = generate_password(length)
    textbox.delete(1.0, "end") # Clear previous content in the textbox
    textbox.insert("end", generated_password)

# Button
button = customtkinter.CTkButton(app, height=50, width=150, fg_color="#33b8ff", text_color = "black", text="Generate Password", command=generate_password_and_update)
button.pack(padx=20, pady=20)

# Textbox
textbox = customtkinter.CTkTextbox(app)
textbox.pack(padx=20, pady=20)

# Label for password length
label = customtkinter.CTkLabel(app, text="Choose password length", corner_radius=8, fg_color="#33b8ff", font=('Arial', 15))
label.pack(padx=10, pady=10)

# Some option list
values = ["8", "12","16", "32"]


# Infinite loop to run the GUI
app.mainloop()
