import tkinter.messagebox
from tkinter import *

import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Books Review")
        self.geometry(f"{2100}x{1080}")  # {1100}x{580}

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # -------------------- create sidebar frame with widgets --------------------------
        # sidebar frame
        self.leftsideBar = customtkinter.CTkFrame(self, corner_radius=15)
        self.leftsideBar.grid(row=0, column=0, rowspan=4, sticky="NSew")

        # titolo
        self.logoLabel = customtkinter.CTkLabel(self.leftsideBar, text="Filtri",
                                                font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logoLabel.grid(row=0, column=0, padx=20, pady=(20, 10))

        # N. massimo elementi
        self.nMaxDocLabel = customtkinter.CTkLabel(self.leftsideBar, text="Numero massimo elementi:", anchor="w")
        self.nMaxDocLabel.grid(row=1, column=0)

        self.nMaxDoc = customtkinter.CTkEntry(master=self.leftsideBar,
                                              placeholder_text="N max",
                                              width=120,
                                              height=25,
                                              border_width=2,
                                              corner_radius=10)
        self.nMaxDoc.grid(row=2, column=0, padx=20, pady=10)

        # Sentiment
        self.sentimentLabel = customtkinter.CTkLabel(self.leftsideBar, text="Sentiment:", anchor="w")
        self.sentimentLabel.grid(row=3, column=0)

        # filtri
        self.sentimentValue = customtkinter.CTkOptionMenu(self.leftsideBar,
                                                          values=["Positive", "Neutral", "Negative"], )
        self.sentimentValue.grid(row=4, column=0, padx=20, pady=10)
        self.sentimentValue.set("Neutral")  # set initial value

        # slider
        self.sentimentSlider = customtkinter.CTkSlider(master=self.leftsideBar, from_=0, to=100)
        self.sentimentSlider.grid(row=5, column=0, padx=20, pady=10)

        # Appearance Mode
        self.appearanceModeLabel = customtkinter.CTkLabel(self.leftsideBar, text="Aspetto:", anchor="w")
        self.appearanceModeLabel.grid(row=6, column=0)
        self.appearanceModeOptionemenu = customtkinter.CTkOptionMenu(self.leftsideBar,
                                                                     values=["Light", "Dark", "System"],
                                                                     command=self.change_appearance_mode_event)
        self.appearanceModeOptionemenu.grid(row=7, column=0)

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
        self.submitQuery = customtkinter.CTkButton(self,
                                                   width=120,
                                                   height=32,
                                                   border_width=0,
                                                   corner_radius=8,
                                                   text="Ricerca")
        self.submitQuery.grid(row=0, column=2, padx=0, pady=(10, 20))

        # frame results
        self.results = customtkinter.CTkFrame(self, corner_radius=15, fg_color='#1a1a1a', border_color='#1a1a1a',
                                              border_width=0)
        self.results.grid(row=1, column=1, rowspan=4, columnspan=2)

        self.mycanvas = Canvas(self.results, width=800, height=450, bg='#1a1a1a', bd=0)
        self.mycanvas.pack(side=LEFT, fill="y")

        self.yscroll = customtkinter.CTkScrollbar(self.results, orientation="vertical", command=self.mycanvas.yview,
                                                  fg_color='#1a1a1a')
        self.yscroll.pack(side=RIGHT, fill="y")

        self.mycanvas.configure(yscrollcommand=self.yscroll.set)
        self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion=self.mycanvas.bbox("all")))

        self.myframe = Frame(self.mycanvas, bg='#1a1a1a', bd=0)
        self.mycanvas.create_window((0, 0), window=self.myframe, anchor="nw")

    # metodi
    def change_appearance_mode_event(self, newAppearanceMode: str):
        customtkinter.set_appearance_mode(newAppearanceMode)


# funzioni
def submit_search():
    query = app.query.get()
    print("Query di ricerca: " + query)
    print("Numero massimo di documenti: " + nMaxDoc.get())
    print("Sentiment value: " + sentimentValue.get())


# --------- Main -----------
if __name__ == "__main__":
    app = App()
    nMaxDoc = tkinter.StringVar()
    sentimentValue = tkinter.StringVar()

    # inizializzazione
    app.submitQuery.configure(command=submit_search)
    app.sentimentValue.configure(variable=sentimentValue)
    app.nMaxDoc.configure(textvariable=nMaxDoc)

    for i in range(50):
        # book frame
        globals()[f"book{i}"] = customtkinter.CTkFrame(app.myframe, corner_radius=15, fg_color='#323332',
                                                       border_width=0)
        globals()[f"book{i}"].grid(row=i, column=0, columnspan=2, pady=5)

        globals()[f"book{i}"].grid_columnconfigure(1, weight=1)
        globals()[f"book{i}"].grid_columnconfigure(2, weight=3)
        globals()[f"book{i}"].grid_columnconfigure(3, weight=1)
        globals()[f"book{i}"].grid_rowconfigure((0, 1, 2), weight=1)

        # creazione copertina
        img = Image.open("media/book_image.jpg")
        img = img.resize((100, 150), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        bookCover = tkinter.Label(globals()[f"book{i}"], image=img)
        bookCover.image = img
        bookCover.grid(row=0, column=1, rowspan=3)

        # Book title
        bookTitle = customtkinter.CTkLabel(globals()[f"book{i}"],
                                           text="Padre ricco, Padre povero",
                                           text_color='#1e538c',
                                           font=(None, 20),
                                           corner_radius=8)
        bookTitle.grid(row=0, column=2)

        # Review
        review = customtkinter.CTkTextbox(globals()[f"book{i}"], width=620, height=150)
        review.grid(row=1, column=2, rowspan=2)
        review.insert("0.0",
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque eu libero in neque blandit pulvinar euismod sed risus. Quisque porttitor magna nulla, ac ultricies justo sagittis a. Duis eget mauris eu elit commodo lacinia sed sit amet lectus. Nulla facilisis felis sit amet est eleifend, id sodales eros hendrerit. Maecenas eros velit, elementum eget pellentesque vel, ullamcorper in justo. Aliquam maximus, lectus et imperdiet consequat, turpis dui fermentum velit, et cursus nisi diam eu ligula. Nulla lacinia molestie odio eu maximus. Mauris a augue at orci consectetur dapibus. Mauris lorem erat, aliquam eu volutpat a, accumsan eget ligula. Nullam eu semper massa, non accumsan ligula.")  # insert at line 0 character 0
        review.configure(state="disabled")

        # Sentiment
        sentiment = customtkinter.CTkLabel(globals()[f"book{i}"],
                                           text="Negative",
                                           text_color='black',
                                           fg_color=("red"),
                                           corner_radius=8)
        # recensione.place(relx=0.5, rely=0.5, anchor=tkinter.N)
        sentiment.grid(row=1, column=3)

    app.mainloop()