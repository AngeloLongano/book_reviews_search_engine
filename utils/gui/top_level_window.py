from tkinter import *
import customtkinter


class ToplevelWindow(customtkinter.CTkToplevel):

    # Costructor
    def __init__(self, app, document):
        """ 
            Costruttore per la classe ToplevelWindow. Creazione widget che compongono la Gui

            :param app: istanza della classe che la richiama
            :param document: lista contenente informazioni sulla recensione
        """
        super().__init__(app)
        self.document = document
        self.geometry("700x450")
        self.title(document["title_book"])

        # Data review
        self.data_review = customtkinter.CTkLabel(self,
                                            text=str(document["date"])[:10],
                                            font=(None, 12),
                                            corner_radius=8)
        self.data_review.grid(row=0, column=2, padx=5)

        # Review Title
        self.review_title = customtkinter.CTkLabel(self,
                                            text=document["title"][:45]+"...",
                                            font=(None, 20),
                                            anchor=NW,
                                            corner_radius=8)
        self.review_title.grid(row=0, column=0)

        # Score
        self.review_score = customtkinter.CTkLabel(self,
                                            text="Score: "+str(document["score"]),
                                            font=(None, 15),
                                            anchor=NW,
                                            corner_radius=8)
        self.review_score.grid(row=1, column=0)

        # Review
        self.review = customtkinter.CTkTextbox(self, width=580, height=300)
        self.review.grid(row=2, column=0)
        self.review.insert("0.0",document["text"])  # insert at line 0 character 0
        self.review.configure(state="disabled")

        # Review Author
        self.review_author = customtkinter.CTkLabel(self,
                                            text=document["name_user"],
                                            text_color='#1e538c',
                                            font=(None, 14),
                                            corner_radius=8)
        self.review_author.grid(row=3, column=0)

        # Sentiment negative
        self.positive_sentiment = customtkinter.CTkLabel(self,
                                            text_color='black',
                                            text=document["positive_sentiment"],
                                            fg_color=("green"),
                                            corner_radius=8)
        # recensione.place(relx=0.5, rely=0.5, anchor=tkinter.N)
        self.positive_sentiment.grid(row=1, column=2, pady=2)

        # Sentiment negative
        self.neutral_sentiment = customtkinter.CTkLabel(self,
                                            text_color='black',
                                            text=document["neutral_sentiment"],
                                            fg_color=("white"),
                                            corner_radius=8)
        # recensione.place(relx=0.5, rely=0.5, anchor=tkinter.N)
        self.neutral_sentiment.grid(row=2, column=2, pady=2)

        # Sentiment negative
        self.negative_sentiment = customtkinter.CTkLabel(self,
                                            text_color='black',
                                            text=document["negative_sentiment"],
                                            fg_color=("red"),
                                            corner_radius=8)
        # recensione.place(relx=0.5, rely=0.5, anchor=tkinter.N)
        self.negative_sentiment.grid(row=3, column=2, pady=2)