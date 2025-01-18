import math  # Get Math Library
from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # For Table Widget
import customtkinter  # Get Customtkinter

# Window Setup
window = customtkinter.CTk()
window._set_appearance_mode("dark")  # Set default appearance mode
window.title("Simple Root Calculator")  # Set Title for Window
window.geometry("700x600")  # Set Geometry for Window
window.resizable(False, False)  # Set Resizable for Window

# Tab View Setup
tabview = customtkinter.CTkTabview(
    master=window, width=700, height=600, corner_radius=25
)
tabview.place(relx=0.5, rely=0.5, anchor=CENTER)

tabview.add("CBR To Num")  # Add tab at the end
tabview.add("Num To CBR")  # Add tab at the end
tabview.add("Num To Num by CBR")  # Add tab at the end
tabview.set("CBR To Num")  # Set currently visible tab

# ================================================================
# Tab 1
def Equation():
    """Calculate cubic root of a number."""
    Entry_Var = float(ent.get())
    Result1 = math.cbrt(Entry_Var)
    ResultLabel.configure(text=f"Cubic Root of {Entry_Var} is : {Result1}")

# ================================================================
# Tab 2
def Equation_2():
    """Convert a number to its cubic closure."""
    Entry_Var_Second = float(ent_2.get())
    Result = math.pow(Entry_Var_Second, 3)
    Floor = math.floor(Result)
    Round = math.ceil(Result)
    ResultLabel_Second.configure(text=f"Closure of {Entry_Var_Second} is : {Floor}")
    print("=======================")
    print("After Floor:", Floor)
    print("Before Floor:", Result)
    print("After Ceil:", Round)
    print("=======================")

# ================================================================
# Tab 3
def Equation_3():
    """Calculate numbers divided by cubic roots and display results in a table."""
    Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Entry_Var_Third = float(ent_3.get())
    First_Result = [Entry_Var_Third / num for num in Numbers]
    First_Result_Sum = [math.pow(num, 3) for num in First_Result]
    Second_Result = [math.floor(num) for num in First_Result_Sum]
    Second_ResultCeiled = [math.ceil(num) for num in First_Result_Sum]

    # Clear table contents
    for item in table.get_children():
        table.delete(item)

    # Populate the table
    for num, ceil,floored in zip(
        Numbers,Second_ResultCeiled, Second_Result
    ):
        table.insert("", "end", values=(num, ceil,floored))

# Clear function
def clear():
    ResultLabel.configure(text="None")
    ResultLabel_Second.configure(text="None")
    for item in table.get_children():
        table.delete(item)


# Font Configuration
font = customtkinter.CTkFont(family="Calibri", size=16, weight="bold")

# ================================================================
# Tab 1 Widgets
customtkinter.CTkLabel(
    tabview.tab("CBR To Num"),
    text="Cubic Root Converter From Cubic Root To Numbers",
    font=font,
    width=700,
).place(relx=0.5, rely=0.1, anchor=CENTER)
ent = customtkinter.CTkEntry(
    tabview.tab("CBR To Num"),
    placeholder_text="Enter your CubicRoot to convert it to Numbers.",
    width=335,
    font=font,
)
ent.place(relx=0.5, rely=0.2, anchor=CENTER)
customtkinter.CTkButton(
    tabview.tab("CBR To Num"), text="Calculate Cubic Root", command=Equation
).place(relx=0.5, rely=0.3, anchor=CENTER)
customtkinter.CTkButton(tabview.tab("CBR To Num"), text="Clear", command=clear).place(
    relx=0.5, rely=0.4, anchor=CENTER
)
ResultLabel = customtkinter.CTkLabel(
    tabview.tab("CBR To Num"), text="None", font=font, width=200
)
ResultLabel.place(relx=0.5, rely=0.6, anchor=CENTER)

# ================================================================
# Tab 2 Widgets
customtkinter.CTkLabel(
    tabview.tab("Num To CBR"),
    text="Cubic Root Converter From Numbers To CubicRoot",
    font=font,
    width=700,
).place(relx=0.5, rely=0.1, anchor=CENTER)
ent_2 = customtkinter.CTkEntry(
    tabview.tab("Num To CBR"),
    placeholder_text="Enter your Number to convert it to CubicRoot.",
    width=335,
    font=font,
)
ent_2.place(relx=0.5, rely=0.2, anchor=CENTER)
customtkinter.CTkButton(
    tabview.tab("Num To CBR"), text="Calculate Cubic Root", command=Equation_2
).place(relx=0.5, rely=0.3, anchor=CENTER)
customtkinter.CTkButton(tabview.tab("Num To CBR"), text="Clear", command=clear).place(
    relx=0.5, rely=0.4, anchor=CENTER
)
ResultLabel_Second = customtkinter.CTkLabel(
    tabview.tab("Num To CBR"), text="None", font=font, width=200
)
ResultLabel_Second.place(relx=0.5, rely=0.6, anchor=CENTER)

# ================================================================
# Tab 3 Widgets
customtkinter.CTkLabel(
    tabview.tab("Num To Num by CBR"),
    text="Cubic Root Converter From Numbers To Numbers by CubicRoot",
    font=font,
    width=700,
).place(relx=0.5, rely=0.05, anchor=CENTER)
ent_3 = customtkinter.CTkEntry(
    tabview.tab("Num To Num by CBR"),
    placeholder_text="Enter your Number to convert it to Numbers By CubicRoot.",
    width=417,
    font=font,
)
ent_3.place(relx=0.5, rely=0.13, anchor=CENTER)
customtkinter.CTkButton(
    tabview.tab("Num To Num by CBR"), text="Calculate Cubic Root", command=Equation_3
).place(relx=0.38, rely=0.2, anchor=CENTER)
customtkinter.CTkButton(
    tabview.tab("Num To Num by CBR"), text="Clear", command=clear
).place(relx=0.62, rely=0.2, anchor=CENTER)

# Table for Tab 3
columns = ("Number","Ceiled Result","Floored Result")
table = ttk.Treeview(
    tabview.tab("Num To Num by CBR"), columns=columns, show="headings", height=10
)
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=150, anchor="center")
table.place(relx=0.5, rely=0.6, anchor=CENTER)

style = ttk.Style()
style.theme_use("default")

table.column("Number", anchor="center", width=100)
table.column("Ceiled Result", anchor="w", width=100)
table.column("Floored Result", anchor="center", width=120)

# Customize the treeview
style.configure(
    "Treeview",
    background="#1c1c1c",  # Background color
    foreground="#ddd",  # Text color
    rowheight=25,  # Row height
    fieldbackground="#1c1c1c",
)  # Field background
style.map(
    "Treeview",
    background=[("selected", "#2F2E2E")],  # Background of selected row
    foreground=[("selected", "white")],
)  # Foreground of selected row

style.configure(
    "Treeview.Heading",
    background="darkgray",  # Header background
    foreground="black",  # Header text color
font=("Calibri", 12, "bold"),
)  # Header font

# ================================================================
window.mainloop()