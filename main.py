import tkinter
import customtkinter
from utils.ManageReviewIndex import MangeReviewIndex
from gui.App import App
from preprocessing.main_preprocessing import preprocessing
import html2text

if __name__ == "__main__":
    your_html_string = "I bought this <b class='match term0'>book</b> because I read some...three. I always buy <b class='match term1'>books</b> in the hope and expectation...However, this <b class='match term0'>book</b> is in urgent need of"
    
    text = html2text.html2text(your_html_string)
    print(text)
    
    preprocessing()

    customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

    app = App()

    
    

    app.mainloop()
