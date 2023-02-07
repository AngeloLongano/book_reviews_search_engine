import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from utils.models.DocumentModel import DocumentModel
from utils.ManageReviewIndex import MangeReviewIndex
from utils.services.path_used_service import IMAGE_PATH


def change_appearance_mode_event(new_mode: str):
    customtkinter.set_appearance_mode(new_mode)

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Books Review")
        self.geometry(f"{1100}x{580}")  # {1100}x{580}

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # -------------------- create sidebar frame with widgets --------------------------
        # sidebar frame
        self.left_side_bar = customtkinter.CTkFrame(self, corner_radius=15)
        self.left_side_bar.grid(row=0, column=0, rowspan=4, sticky="NSew")

        # titolo
        self.label_logo = customtkinter.CTkLabel(self.left_side_bar, text="Filtri",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_logo.grid(row=0, column=0, padx=20, pady=(20, 10))

        # N. massimo elementi
        self.num_max_docs_label = customtkinter.CTkLabel(self.left_side_bar, text="Numero massimo elementi:",
                                                         anchor="w")
        self.num_max_docs_label.grid(row=1, column=0)

        self.num_max_docs = customtkinter.CTkEntry(master=self.left_side_bar,
                                                   placeholder_text="N max",
                                                   width=120,
                                                   height=25,
                                                   border_width=2,
                                                   corner_radius=10)
        self.num_max_docs.grid(row=2, column=0, padx=20, pady=10)

        # Sentiment
        self.sentiment_label = customtkinter.CTkLabel(self.left_side_bar, text="Sentiment:", anchor="w")
        self.sentiment_label.grid(row=3, column=0)

        # filtri
        self.sentiment_value = customtkinter.CTkOptionMenu(self.left_side_bar,
                                                           values=["Positive", "Neutral", "Negative"], )
        self.sentiment_value.grid(row=4, column=0, padx=20, pady=10)
        self.sentiment_value.set("Neutral")  # set initial value

        # slider
        self.sentiment_slider = customtkinter.CTkSlider(master=self.left_side_bar, from_=0, to=100)
        self.sentiment_slider.grid(row=5, column=0, padx=20, pady=10)

        # Appearance Mode
        self.appearance_model_label = customtkinter.CTkLabel(self.left_side_bar, text="Aspetto:", anchor="w")
        self.appearance_model_label.grid(row=6, column=0)
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.left_side_bar,
                                                                values=["Light", "Dark", "System"],
                                                                command=change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0)

        # ------------------- Right Frame ----------------------
        # input search
        self.query = customtkinter.CTkEntry(self,
                                            placeholder_text="Ricerca",
                                            width=600,
                                            height=35,
                                            border_width=2,
                                            corner_radius=10)
        self.query.grid(row=0, column=1, padx=20, pady=(10, 20))

        # submit search
        self.submit_query = customtkinter.CTkButton(self,
                                                    width=120,
                                                    height=32,
                                                    border_width=0,
                                                    corner_radius=8,
                                                    text="Ricerca")
        self.submit_query.grid(row=0, column=2, padx=0, pady=(10, 20))

        # frame results
        self.results = customtkinter.CTkFrame(self, corner_radius=15, fg_color='#1a1a1a', border_color='#1a1a1a',
                                              border_width=0)
        self.results.grid(row=1, column=1, rowspan=4, columnspan=2)

        self.my_canvas = Canvas(self.results, width=800, height=450, bg='#1a1a1a', bd=0, highlightthickness=0)
        self.my_canvas.pack(side=LEFT, fill="y")

        self.yscroll = customtkinter.CTkScrollbar(self.results, orientation="vertical", command=self.my_canvas.yview,
                                                   fg_color='#1a1a1a')
        self.yscroll.pack(side=RIGHT, fill="y")

        self.my_canvas.configure(yscrollcommand=self.yscroll.set)
        self.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        self.my_frame = Frame(self.my_canvas, bg='#1a1a1a', bd=0)
        self.my_canvas.create_window((0, 0), window=self.my_frame, anchor="nw")
        self.my_frame.children

    def open_book_model(self):
        self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed

    # metodi
    def crea_libro(self, riga, document: DocumentModel):
        # book frame
        self.book = customtkinter.CTkFrame(self.my_frame, corner_radius=15, fg_color='#323332',border_width=0)
        self.book.grid(row=riga, column=0, columnspan=2, pady=5)

        self.book.grid_columnconfigure(1, weight=1)
        self.book.grid_columnconfigure(2, weight=3)
        self.book.grid_columnconfigure(3, weight=1)
        self.book.grid_rowconfigure((0, 1, 2), weight=1)

        # Book title
        book_title = customtkinter.CTkLabel(self.book,
                                            text=document["title_book"],
                                            text_color='#1e538c',
                                            font=(None, 20),
                                            corner_radius=8)
        book_title.grid(row=0, column=0)

        # Review
        review = customtkinter.CTkTextbox(self.book, width=620, height=150)
        review.grid(row=1, column=2, rowspan=2)
        review.insert("0.0",document["text"])  # insert at line 0 character 0
        review.configure(state="disabled")

        # Sentiment
        sentiment = customtkinter.CTkLabel(self.book,
                                            text=document["negative_sentiment"],
                                            text_color='black',
                                            fg_color=("red"),
                                            corner_radius=8)
        # recensione.place(relx=0.5, rely=0.5, anchor=tkinter.N)
        sentiment.grid(row=1, column=3)

        self.open_book_info = customtkinter.CTkButton(self.book,
                                                    width=120,
                                                    height=32,
                                                    command= self.open_book_model,
                                                    border_width=0,
                                                    corner_radius=8,
                                                    text="Ricerca")
        self.open_book_info.grid(row=1, column=4, padx=0, pady=(10, 20))


    def submit_search(self):
        query = self.query.get()
        print("Query di ricerca: " + query)

        index_manager = MangeReviewIndex()
        index_manager.initialize_index()

        index=0
        query_results = index_manager.search_index(query,"text")
        
        for i in query_results:
            self.crea_libro(index, i)
            index+=1
        # print("Numero massimo di documenti: " + num_max_docs.get())
        # print("Sentiment value: " + sentiment_value.get())

    
