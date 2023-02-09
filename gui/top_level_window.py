import tkinter
from tkinter import *
import customtkinter

class ToplevelWindow(customtkinter.CTkToplevel):

    # Costructor
    def __init__(self, app, document):
        super().__init__(app)
        self.document = document
        self.geometry("580x300")
        self.title()

        # Review

        #self.review = customtkinter.CTkLabel(self, width=620, height=130,text=document["text"])
        #self.review.grid(row=0, column=0)
        #self.review.insert("0.0",document["text"])  # insert at line 0 character 0
        #self.review.configure(state="disabled")

        self.review = customtkinter.CTkTextbox(self, width=580, height=300)
        self.review.grid(row=2, column=0)
        self.review.insert("0.0",document["text"])  # insert at line 0 character 0
        self.review.configure(state="disabled")