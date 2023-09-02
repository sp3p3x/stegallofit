import os, subprocess
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkToolTip import CreateToolTip
from tkinterdnd2 import TkinterDnD, DND_FILES

tempPath = "foo.txt"

banner = '''
███████╗████████╗███████╗ ██████╗  █████╗ ██╗     ██╗      ██████╗ ███████╗██╗████████╗
██╔════╝╚══██╔══╝██╔════╝██╔════╝ ██╔══██╗██║     ██║     ██╔═══██╗██╔════╝██║╚══██╔══╝
███████╗   ██║   █████╗  ██║  ███╗███████║██║     ██║     ██║   ██║█████╗  ██║   ██║   
╚════██║   ██║   ██╔══╝  ██║   ██║██╔══██║██║     ██║     ██║   ██║██╔══╝  ██║   ██║   
███████║   ██║   ███████╗╚██████╔╝██║  ██║███████╗███████╗╚██████╔╝██║     ██║   ██║   
╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝   ╚═╝   

-----------------------Developed & Maintained by @sp3p3x @ask--------------------------
'''

class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left', background='yellow', relief='solid', borderwidth=1, font=("times", "8", "normal"))
        label.pack(ipadx=1)

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()

class Steg():

    def binwalk(path):
        print("\nBINWALK")
        output = os.system("binwalk " + path)
        print(output)
        print("_______________________________________\n")

    def exiftool(path):
        print("EXIFTOOL \n")
        output = os.system("exiftool " + path)
        print(output)
        print("_______________________________________\n")

    def stegsnow(path):
        print("STEGSNOW\n")
        p = input("Password: ")
        cmd = " -C -p" + p + " " +  path
        output = os.system("stegsnow" + cmd)
        print(output)
        print("_______________________________________\n")

    def pngSteg(path):
        pass

    def jpgSteg(path):
        pass

    def txtSteg(path):
        stegsnow(path)

    def imageSteg(path):
        binwalk(path)
        exiftool(path)

    def audioSteg(path):
        pass

class UI():

    colours=["#2A2F32","#0D8ABF","#02C39A"]

    def __init__(self):
        self.window=TkinterDnD.Tk()
        self.window.geometry("600x600")
        self.window.title("stegallofit")
        self.window.configure(bg=self.colours[0])
        self.window.resizable(height=0, width=0)

    def mainUI(self):    

        def dnd_listbox(self, event):
            self.listb.insert("end", event.data)

        listb=tk.Listbox(self.window, selectmode=tk.SINGLE, bg=self.colours[0], fg=self.colours[2], font=("Roboto" , 10, 'bold'), height=23, width=70, borderwidth=5)

        DnD_icon=tk.Label(self.window, bg=self.colours[0])
        DnD_label=tk.Label(self.window, text="DROP THE CSV FILE",font=("Roboto" , 8, 'bold'), bg=self.colours[0], fg=self.colours[1])
        DnD_icon.drop_target_register(DND_FILES)
        listb.drop_target_register(DND_FILES)
        DnD_icon.dnd_bind("<<Drop>>", dnd_listbox)
        listb.dnd_bind("<<Drop>>", dnd_listbox)

        listb.place(x=50, y=90)
        DnD_icon.place(x=252, y=210)
        DnD_label.place(x=250, y=300)

    def run(self):
        self.mainUI()
        self.window.mainloop()

def main():
    print(banner)

    while True:
        # inpFilePath = str(input('Image path: '))
        inpFilePath = str(tempPath)
        
        if inpFilePath.endswith('.png'):
            print("Input file path: " + inpFilePath + "\n")
            Steg.imageSteg(inpFilePath)
            Steg.pngSteg(inpFilePath)
        elif inpFilePath.endswith('.jpg') or inpFilePath.endswith('.jpeg'):
            print("Input file path: " + inpFilePath + "\n")
            Steg.imageSteg(inpFilePath)
            Steg.jpgSteg(inpFilePath)
        elif inpFilePath.endswith('.txt'):
            print("Input file path: " + inpFilePath + "\n")
            Steg.txtSteg(inpFilePath)    
        elif inpFilePath.endswith('.wav') or inpFilePath.endswith('.mp3')  or inpFilePath.endswith('.mp3'):
            print("Input file path: " + inpFilePath + "\n")
            Steg.audioSteg(inpFilePath)
        else:
            print("Please enter a valid file path!")
            continue

        break


if __name__ == "__main__":
    ui = UI()
    ui.run()