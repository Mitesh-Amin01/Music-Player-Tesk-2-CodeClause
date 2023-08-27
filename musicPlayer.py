from tkinter import *
import pygame
import os
import threading
import time
from mutagen.mp3 import MP3
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror,askquestion,showinfo
from tkinter import ttk
from PIL import Image,ImageTk

class Player:
    def __init__(self,master):
        self.master = master
        pygame.init()
        pygame.mixer.init()
        
        def getIcon():
            self.winicon = PhotoImage(file="img\\best.png")
            master.iconphoto(False,self.winicon)
        
        def icon():
            threads = threading.Thread(target=getIcon)
            threads.start()
        icon()
        
        PLAY = "►"
        PAUSE = "║║"
        RWD = "⏮"
        FWD = "⏭"
        STOP = "■"
        UNPAUSE = "||"
        mute = "🔇"
        unmute = u"\U0001F50A"
        vol_mute = 0.0
        vol_unmute = 1
        
        self.scroll = Scrollbar(master)
        self.playList= Listbox(master,font="Sasarif 12 bold",bd=5,bg="white",width=37,height=19,selectbackground="balck")

def main():
    root = Tk()
    ui = Player(root)
    
    root.geometry("963x470+200+100")
    root.title("MP3 Music Player")
    root.configure(bg="black")
    root.resizable(width=0,height=0)
    root.mainloop()
    
if __name__ == "__main__":
    main()