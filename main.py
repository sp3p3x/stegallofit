import os, subprocess
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.scrolledtext as scrolledtext
from tkinterdnd2 import TkinterDnD, DND_FILES

DEBUG = False

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
        cmnd = "binwalk "+path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def exiftool(self, path):
        cmnd = "exiftool "+path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def stegsnow(self, path):
        print("STEGSNOW\n")
        p = input("Password: ")
        cmd = " -C -p" + p + " " +  path
        output = os.system("stegsnow" + cmd)
        print(output)

    def steghide(self, path):
        p = input("Password: ")
        cmnd = "steghide extract -sf -p" + p + " " +  path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        print(output)
        return output
    
    def stegseek(self, path):
        w = input("wordlist: ")
        cmnd = "stegseek " + path + " " + w
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        print(output)
        return output
    
    def foremost(self, path):
        cmnd = "foremost "+path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output
    
    def stegoveritas(self, path):
        f = path.split("/")
        out_path = input()
        cmnd = "stegoveritas  "+ path + " -out "+ out_path + "/" + f[-1] + "_extracted"
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def strings(self, path):
        cmnd = "strings "+path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def pngcheck(self,path):
        cmnd = "pngcheck -v "+path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def jsteg(self,path):
        cmnd = "jsteg -reveal " + path + " output"
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def pngSteg(self, path):
        binwalkOut = self.binwalk(path)
        exiftoolOut = self.exiftool(path)
        stringsOut = self.strings(path)
        pngcheckOut = self.pngcheck(path)
        out = {"binwalk":binwalkOut, "exiftool":exiftoolOut, "strings":stringsOut, "pngcheck":pngcheckOut}

        return out

    def jpgSteg(self, path):
        binwalkOut = self.binwalk(path)
        exiftoolOut = self.exiftool(path)
        stringsOut = self.strings(path)
        out = {"binwalk":binwalkOut, "exiftool":exiftoolOut, "strings":stringsOut, "pngcheck":pngcheckOut}

        return out

    def txtSteg(self, path):
        stegsnowOut = self.stegsnow(path)

        out = {"stegsnow":stegsnowOut}

        return out

    def imageSteg(self, path):
        binwalkOut = self.binwalk(path)
        exiftoolOut = self.exiftool(path)
        stringsOut = self.strings(path)
        pngcheckOut = self.pngcheck(path)
        out = {"binwalk":binwalkOut, "exiftool":exiftoolOut, "strings":stringsOut, "pngcheck":pngcheckOut}

        return out

    def audioSteg(self, path):
        pass

    def genericSteg(self, path):
        stringsOut = self.strings(path)

        out = {"strings":stringsOut}

        return out

class UI():

    colours=["#1E2233","#36827F","#F9DB6D"]

    def __init__(self):
        self.window=TkinterDnD.Tk()
        self.window.geometry("600x600")
        self.window.title("stegallofit")
        self.window.configure(bg=self.colours[0])
        self.window.resizable(height=0, width=0)

    def mainUI(self):

        widgets = []

        def destroy():
            for widget in widgets:
                widget.place_forget()

        def dnd_listbox(event):
            listb.insert("end", event.data)

        def choose_file():
            self.window.filename = filedialog.askopenfilename(initialdir="Documents", title="Select file", filetypes=[("select png files","*.png")])
            listb.insert("end", self.window.filename)

        def nextUI():
            try:
                inpFilePath = '"' + listb.get(listb.curselection()).rstrip('}').lstrip('{') + '"'
                destroy()
                self.ouputUI(inpFilePath)
            except Exception as err:
                if DEBUG:
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
        widgets.append(banner_label)
        banner_label.place(x=150, y=10)

        credits_label=tk.Label(self.window, text="Developed and maintained by @sp3p3x @ask",font=("Roboto" , 9, 'bold'), bg=self.colours[0], fg=self.colours[2])
        widgets.append(credits_label)
        credits_label.place(x=147, y=55)

        choose_file_button=tk.Button(self.window,command=lambda: choose_file(), text="CHOOSE FILE",font=("Roboto" , 10, 'bold') , bg=self.colours[1], activebackground=self.colours[2])
        widgets.append(choose_file_button)
        choose_file_button.place(x=110, y=460)

        clear_button=tk.Button(self.window,command=lambda: clear(), text="CLEAR",font=("Roboto" , 10, 'bold') , bg=self.colours[1], activebackground=self.colours[2])
        widgets.append(clear_button)
        clear_button.place(x=260, y=460)

        clear_all_button=tk.Button(self.window,command=lambda: clearAll(), text="CLEAR ALL",font=("Roboto" , 10, 'bold') , bg=self.colours[1], activebackground=self.colours[2])
        widgets.append(clear_all_button)
        clear_all_button.place(x=360, y=460)

        next_button=tk.Button(self.window,command=lambda: nextUI(), height=2, width=9, bg=self.colours[0], fg=self.colours[1], activebackground=self.colours[2], text="NEXT", font=("Roboto" , 10, 'bold'))
        widgets.append(next_button)
        next_button.place(x=240, y=530)

        DnD_label=tk.Label(self.window, text="DROP THE FILE",font=("Roboto" , 8, 'bold'), bg=self.colours[0], fg=self.colours[1])
        widgets.append(DnD_label)
        DnD_label.place(x=250, y=300)


        # DnD_icon=tk.Label(self.window, bg=self.colours[0])
        # DnD_icon.place(x=252, y=210)

        # DnD_icon.drop_target_register(DND_FILES)
        # DnD_icon.dnd_bind("<<Drop>>", dnd_listbox)

        listb.drop_target_register(DND_FILES)
        listb.dnd_bind("<<Drop>>", dnd_listbox)
        widgets.append(listb)
        listb.place(x=50, y=90)

        # todo: add dnd hook to label

        CreateToolTip(DnD_label,"Drop the files here!")


    def ouputUI(self, inpFilePath):

        widgets = []

        def destroy():
            for widget in widgets:
                widget.place_forget()

        def nextUI():
            destroy()
            self.mainUI()

        def modifyText(newText):
            outputBox.config(state=NORMAL)
            outputBox.delete('1.0',END)
            outputBox.insert(END, newText)
            outputBox.config(state=DISABLED)

        def classify():
            try:
                steg = Steg()
                if inpFilePath.rstrip('"').endswith('.png'):
                    if DEBUG:
                        print("Input file path: " + inpFilePath + "\n")
                    outData = steg.pngSteg(inpFilePath)
                elif inpFilePath.rstrip('"').endswith('.jpg') or inpFilePath.endswith('.jpeg'):
                    if DEBUG:
                        print("Input file path: " + inpFilePath + "\n")
                    outData = steg.jpgSteg(inpFilePath)
                elif inpFilePath.rstrip('"').endswith('.txt'):
                    if DEBUG:
                        print("Input file path: " + inpFilePath + "\n")
                    outData = steg.txtSteg(inpFilePath)    
                elif inpFilePath.rstrip('"').endswith('.wav') or inpFilePath.endswith('.mp3'):
                    if DEBUG:
                        print("Input file path: " + inpFilePath + "\n")
                    outData = steg.audioSteg(inpFilePath)
                else:
                    if DEBUG:
                        print("Input file path: " + inpFilePath + "\n")
                    outData = steg.genericSteg(inpFilePath)

                return outData

            except Exception as err:
                if DEBUG:
                    print(err)

        outData = classify()
        outDataKeys = [string.upper() for string in list(outData.keys())]

        def initOut():
            modifyText(list(outData.values())[0])

        def changeTool(*args):
            toolName = selectedTool.get().lower()
            modifyText(outData[toolName])

        outputBox = scrolledtext.ScrolledText(self.window,  state=DISABLED, bg=self.colours[0], fg=self.colours[2], bd=2, height=25, width=66, font=("Roboto" , 9, 'bold'), padx=10, pady=5)
        outputBox.vbar.config(troughcolor = self.colours[0], background=self.colours[1], width=14, activebackground=self.colours[2])
        widgets.append(outputBox)
        outputBox.place(x=16, y=100)

        selectedTool = StringVar(self.window)
        selectedTool.set(outDataKeys[0])

        dropdownStyle = ttk.Style()

        self.window.option_add('*TCombobox*Listbox*Background', self.colours[0])
        self.window.option_add('*TCombobox*Listbox*Foreground', self.colours[2])
        self.window.option_add('*TCombobox*Listbox*selectBackground', self.colours[1])
        self.window.option_add('*TCombobox*Listbox*selectForeground', self.colours[2])
        dropdownStyle.map('TCombobox', fieldbackground=[('readonly', self.colours[0])])
        dropdownStyle.map('TCombobox', selectbackground=[('readonly', self.colours[0])])
        dropdownStyle.map('TCombobox', selectforeground=[('readonly', self.colours[2])])
        dropdownStyle.map('TCombobox', background=[('readonly', self.colours[0])])
        dropdownStyle.map('TCombobox', foreground=[('readonly', self.colours[2])])

        toolNameDropdown = ttk.Combobox(self.window, textvariable=selectedTool, justify='center')
        toolNameDropdown['values']=outDataKeys
        toolNameDropdown.configure(font=("Roboto" , 12, 'bold'), state="readonly")
        toolNameDropdown.bind("<<ComboboxSelected>>", lambda e: toolNameDropdown.selection_clear())
        
        widgets.append(toolNameDropdown)
        toolNameDropdown.place(x=170, y=530)

        selectedTool.trace('w', changeTool)

        initOut()

        back_button=tk.Button(self.window,command=lambda: nextUI(), height=1, width=8, bg=self.colours[0], fg=self.colours[1], activebackground=self.colours[2], text="BACK", font=("Roboto" , 10, 'bold'))
        widgets.append(back_button)
        back_button.place(x=20, y=30)

    def run(self):
        self.mainUI()
        self.window.mainloop()

def main():
    ui = UI()
    ui.run()

if __name__ == "__main__":
    main()