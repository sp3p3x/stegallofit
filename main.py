import os, subprocess
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES

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

    def binwalk(self, path):
        print("\nBINWALK")
        output = os.system("binwalk " + path)
        return output

    def exiftool(self, path):
        print("EXIFTOOL \n")
        output = os.system("exiftool " + path)
        print(output)
        print("_______________________________________\n")

    def stegsnow(self, path):
        print("STEGSNOW\n")
        p = input("Password: ")
        cmd = " -C -p" + p + " " +  path
        output = os.system("stegsnow" + cmd)
        print(output)
        print("_______________________________________\n")


    def strings(self, path):
        print("STRINGS \n")
        output = os.system("strings " + path)
        print(output)
        print("_______________________________________\n")


    def pngcheck(self,path):
        print("PNGCHECK \n")
        output = os.system("pngcheck -v " + path)
        print(output)
        print("_______________________________________\n")

    def jsteg(self,path):
        print("JSTEG \n")
        output = os.system("jsteg -reveal " + path + " output")
        print(output)
        print("_______________________________________\n")

    def pngSteg(self, path):
        pass

    def jpgSteg(self, path):
        pass

    def txtSteg(self, path):
        self.stegsnow(path)

    def imageSteg(self, path):
        self.binwalk(path)
        self.exiftool(path)
        self.strings(path)
        self.pngcheck(path)

    def audioSteg(self, path):
        pass

class UI():

    colours=["#1E2233","#36827F","#F9DB6D"]

    def __init__(self):
        self.window=TkinterDnD.Tk()
        self.window.geometry("600x600")
        self.window.title("stegallofit")
        self.window.configure(bg=self.colours[0])
        self.window.resizable(height=0, width=0)

    def mainUI(self):    

        def dnd_listbox(event):
            listb.insert("end", event.data)

        def choose_file():
            self.window.filename = filedialog.askopenfilename(initialdir="Documents", title="Select file", filetypes=[("select png files","*.png")])
            listb.insert("end", self.window.filename)
        
        def classify():
            try:
                rawInpFilePath = listb.get(listb.curselection()).rstrip('}').lstrip('{')
                inpFilePath = '"' + listb.get(listb.curselection()).rstrip('}').lstrip('{') + '"'
                steg = Steg()
                if rawInpFilePath.endswith('.png'):
                    print("Input file path: " + inpFilePath + "\n")
                    steg.imageSteg(inpFilePath)
                    steg.pngSteg(inpFilePath)
                elif rawInpFilePath.endswith('.jpg') or inpFilePath.endswith('.jpeg'):
                    print("Input file path: " + inpFilePath + "\n")
                    steg.imageSteg(inpFilePath)
                    steg.jpgSteg(inpFilePath)
                elif rawInpFilePath.endswith('.txt'):
                    print("Input file path: " + inpFilePath + "\n")
                    steg.txtSteg(inpFilePath)    
                elif rawInpFilePath.endswith('.wav') or inpFilePath.endswith('.mp3'):
                    print("Input file path: " + inpFilePath + "\n")
                    steg.audioSteg(inpFilePath)
                else:
                    print("Please enter a valid file path!")
            except Exception as err:
                print(err)

        listb=tk.Listbox(self.window, selectmode=tk.SINGLE, bg=self.colours[0], fg=self.colours[2], font=("Roboto" , 10, 'bold'), height=23, width=55, borderwidth=5)

        def clear():
            selection = listb.curselection()
            try:
                listb.delete(selection)
            except:
                pass

        def clearAll():
            list_size=listb.size()
            listb.delete(0, list_size)

        banner_label=tk.Label(self.window, text="STEGALLOFIT",font=("Roboto" , 30, 'bold'), bg=self.colours[0], fg=self.colours[2])
        credits_label=tk.Label(self.window, text="Developed and maintained by @sp3p3x @ask",font=("Roboto" , 9, 'bold'), bg=self.colours[0], fg=self.colours[2])
        choose_file_button=tk.Button(self.window,command=lambda: choose_file(), text="CHOOSE FILE",font=("Roboto" , 10, 'bold') , bg=self.colours[1], activebackground=self.colours[2])
        clear_button=tk.Button(self.window,command=lambda: clear(), text="CLEAR",font=("Roboto" , 10, 'bold') , bg=self.colours[1], activebackground=self.colours[2])
        clear_all_button=tk.Button(self.window,command=lambda: clearAll(), text="CLEAR ALL",font=("Roboto" , 10, 'bold') , bg=self.colours[1], activebackground=self.colours[2])
        next_button=tk.Button(self.window,command=lambda: classify(), height=2, width=9, bg=self.colours[0], fg=self.colours[1], activebackground=self.colours[2], text="NEXT", font=("Roboto" , 10, 'bold'))
        DnD_icon=tk.Label(self.window, bg=self.colours[0])
        DnD_label=tk.Label(self.window, text="DROP THE FILE",font=("Roboto" , 8, 'bold'), bg=self.colours[0], fg=self.colours[1])
        DnD_icon.drop_target_register(DND_FILES)
        listb.drop_target_register(DND_FILES)
        DnD_icon.dnd_bind("<<Drop>>", dnd_listbox)
        listb.dnd_bind("<<Drop>>", dnd_listbox)

        CreateToolTip(DnD_label,"Drop the files here!")

        banner_label.place(x=150, y=10)
        credits_label.place(x=147, y=55)
        choose_file_button.place(x=80, y=460)
        clear_button.place(x=220, y=460)
        clear_all_button.place(x=300, y=460)
        listb.place(x=50, y=90)
        DnD_icon.place(x=252, y=210)
        DnD_label.place(x=250, y=300)
        next_button.place(x=240, y=530)
        
    def run(self):
        self.mainUI()
        self.window.mainloop()

def main():
    ui = UI()
    ui.run()

if __name__ == "__main__":
    main()