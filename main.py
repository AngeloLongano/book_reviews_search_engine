import customtkinter

from gui.App import App
from preprocessing.main_preprocessing import preprocessing

if __name__ == "__main__":
    
    preprocessing()

    customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

    app = App()

    
    

    app.mainloop()
