import tkinter

import customtkinter

from gui.App import App
from preprocessing.main_preprocessing import preprocessing

if __name__ == "__main__":
    preprocessing()

    customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

    app = App()
    num_max_docs = tkinter.StringVar()
    sentimentValue = tkinter.StringVar()

    # inizializzazione
    app.submit_query.configure(command=app.submit_search)
    app.sentiment_value.configure(variable=sentimentValue)
    app.num_max_docs.configure(textvariable=num_max_docs)
    app.crea_libri()

    app.mainloop()
