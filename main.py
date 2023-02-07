import tkinter

import customtkinter

from gui.App import App
from preprocessing.main_preprocessing import preprocessing

if __name__ == "__main__":
    preprocessing()

    customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

    app = App()
    nMaxDoc = tkinter.StringVar()
    sentimentValue = tkinter.StringVar()

    # inizializzazione
    app.submitQuery.configure(command=app.submit_search)
    app.sentimentValue.configure(variable=sentimentValue)
    app.nMaxDoc.configure(textvariable=nMaxDoc)
    app.crea_libri()

    app.mainloop()
