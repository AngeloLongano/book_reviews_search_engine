import customtkinter
from utils.gui.App import App
from utils.preprocessing.main_preprocessing import preprocessing

if __name__ == "__main__":
    
    preprocessing()

    app = App()

    app.mainloop()
