from tkinter import *

import customtkinter
import html2text

from utils.ManageReviewIndex import MangeReviewIndex
from utils.gui.top_level_window import ToplevelWindow
from utils.models.DocumentModel import DocumentModel


class App(customtkinter.CTk):

    # costruttore
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
                                                           values=["None", "Positive", "Neutral", "Negative"], )
        self.sentiment_value.grid(row=4, column=0, padx=20, pady=10)
        self.sentiment_value.set("None")

        # Sort By
        self.sort_by_label = customtkinter.CTkLabel(self.left_side_bar, text="Sort by:", anchor="w")
        self.sort_by_label.grid(row=5, column=0)

        self.sort_by = customtkinter.CTkOptionMenu(self.left_side_bar,
                                                   values=["Price", "Negative", "Neutral", "Positive", "Score",
                                                           "Date"], )
        self.sort_by.grid(row=6, column=0, padx=20, pady=10)

        self.reverse = customtkinter.CTkSwitch(master=self.left_side_bar, text="Reverse Sort", onvalue="on",
                                               offvalue="off")
        self.reverse.grid(row=7, column=0, padx=20, pady=10)

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

        # number of results
        self.results_number = customtkinter.CTkLabel(self, text="", anchor="w")
        self.results_number.grid(row=1, column=1)

        # frame results
        self.results = customtkinter.CTkFrame(self, corner_radius=15, fg_color='#1a1a1a', border_color='#1a1a1a',
                                              border_width=0)
        self.results.grid(row=2, column=1, rowspan=4, columnspan=2)

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

        # inizializzazione
        self.submit_query.configure(command=self.submit_search)

    # info book
    def open_book_model(self, document):
        self.toplevel_window = ToplevelWindow(self, document)  # create window if its None or destroyed

    # create book
    def crea_libro(self, riga, document: DocumentModel):
        # book frame
        self.book = customtkinter.CTkFrame(self.my_frame, corner_radius=15, fg_color='#323332', border_width=0)
        self.book.grid(row=riga, column=0, columnspan=2, pady=5)

        self.book.grid_columnconfigure((0, 1, 2), weight=1)
        self.book.grid_rowconfigure((0, 1, 2), weight=1)

        # Book title
        my_font = customtkinter.CTkFont(size=20, weight='bold')
        self.book_title = customtkinter.CTkLabel(self.book,
                                                 text=document["title_book"][:45] + "...",
                                                 text_color='#1e538c',
                                                 font=my_font,
                                                 justify="left",
                                                 corner_radius=8)
        self.book_title.grid(row=0, column=0, pady=20)

        # Data review
        self.data_review = customtkinter.CTkLabel(self.book,
                                                  text=str(document["date"])[:10],
                                                  font=(None, 12),
                                                  corner_radius=8)
        self.data_review.grid(row=0, column=2, padx=5)

        # Review Title
        title_score = document["title"][:45] + "..., Score:" + str(document["score"])

        self.review_title = customtkinter.CTkLabel(self.book,
                                                   text=title_score,
                                                   font=(None, 15),
                                                   anchor=NW,
                                                   corner_radius=8)
        self.review_title.grid(row=1, column=0)

        # Review
        self.review = customtkinter.CTkTextbox(self.book, width=620, height=130)
        self.review.grid(row=2, column=0)
        text_highlights = html2text.html2text(document["highlights"])
        self.review.insert("0.0", text_highlights)  # insert at line 0 character 0
        self.review.configure(state="disabled")

        # Review Author
        self.review_author = customtkinter.CTkLabel(self.book,
                                                    text=document["name_user"],
                                                    text_color='#1e538c',
                                                    font=(None, 14),
                                                    corner_radius=8)
        self.review_author.grid(row=3, column=0)

        # Sentiment
        self.sentiment = customtkinter.CTkLabel(self.book,
                                                text_color='black',
                                                corner_radius=8)
        # recensione.place(relx=0.5, rely=0.5, anchor=tkinter.N)
        self.sentiment.grid(row=1, column=2)

        if (document["negative_sentiment"] > document["neutral_sentiment"] and document["negative_sentiment"] >
                document["positive_sentiment"]):
            self.sentiment.configure(text=document["negative_sentiment"], fg_color=("red"))

        elif (document["neutral_sentiment"] > document["negative_sentiment"] and document["neutral_sentiment"] >
              document["positive_sentiment"]):
            self.sentiment.configure(text=document["neutral_sentiment"], fg_color=("white"))

        elif (document["positive_sentiment"] > document["negative_sentiment"] and document["positive_sentiment"] >
              document["neutral_sentiment"]):
            self.sentiment.configure(text=document["positive_sentiment"], fg_color=("green"))

        # Open book info
        self.open_book_info = customtkinter.CTkButton(self.book,
                                                      width=80,
                                                      height=32,
                                                      command=lambda: self.open_book_model(document),
                                                      border_width=0,
                                                      corner_radius=8,
                                                      text="Full review")
        self.open_book_info.grid(row=2, column=2, padx=0, pady=(10, 20))

    # print error
    def print_error(self, query_corretta):
        # Errore print
        my_font = customtkinter.CTkFont(size=20, weight='bold')
        self.error = customtkinter.CTkLabel(self.my_frame,
                                            text="Your search returned no results in any documents.",
                                            text_color='#1e538c',
                                            font=my_font,
                                            justify="left",
                                            corner_radius=8)
        self.error.grid(row=0, column=0, pady=20)

        self.query_corretta = customtkinter.CTkLabel(self.my_frame,
                                                     text="Did you mean: " + query_corretta + "?",
                                                     text_color='#1e538c',
                                                     font=my_font,
                                                     justify="left",
                                                     corner_radius=8)
        self.query_corretta.grid(row=1, column=0, pady=20)

    # submit search
    def submit_search(self):
        # take value from GUI
        query = self.query.get()
        reverse = self.reverse.get()
        num_max_docs = self.num_max_docs.get()
        sentiment_value = self.sentiment_value.get()
        sorted_by = self.sort_by.get()

        # remove results of previus query
        self.delete_books()

        sort_name_corrispondence = {"Price": "price_book", "Negative": "negative_sentiment",
                                    "Neutral": "neutral_sentiment", "Positive": "positive_sentiment", "Score": "score",
                                    "Date": "date", "None": "None"}

        # reverse
        if reverse == "off":
            reverse = 0
        else:
            reverse = 1

        # n max documents
        if num_max_docs == "" or num_max_docs <= "0":
            num_max_docs = 10
        else:
            num_max_docs = int(num_max_docs)

        print("parametri: ", "query:", query, "reverse:", reverse, "num max docs:", num_max_docs, "sentiment:",
              sentiment_value, "soretd by:", sorted_by)

        index_manager = MangeReviewIndex()
        query_corretta = index_manager.correct_query(query)

        index = 0
        query_results = index_manager.search_index(query, "text", sort_name_corrispondence[sentiment_value],
                                                   num_max_docs, reverse, sort_name_corrispondence[sorted_by])

        self.results_number.configure(text="About " + str(len(query_results)) + " results")

        if query_results:
            for i in query_results:
                self.crea_libro(index, i)
                index += 1
        else:
            self.print_error(query_corretta)

    # remove book
    def delete_books(self):
        for child in self.my_frame.winfo_children():
            child.destroy()
