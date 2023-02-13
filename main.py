from utils.gui.App import App
from utils.preprocessing.main_preprocessing import preprocessing

if __name__ == "__main__":
    
    #Fase di preprocessing
    preprocessing()
    #Inizializzazione Gui
    app = App()
    
    app.mainloop()
