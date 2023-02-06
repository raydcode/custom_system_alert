import tkinter as tk
from tkinter import messagebox




def alert(title,message):
    response = messagebox.showinfo(title,message)
    

alert("Alert", "Hey Good Morning ! ")
