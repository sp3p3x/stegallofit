import os, subprocess
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.scrolledtext as scrolledtext
from tkinterdnd2 import TkinterDnD, DND_FILES
import string

DEBUG = True

userInput = {}


def debug(text):
    if text == "b":
        input()
    elif DEBUG:
        print(text)


class CreateToolTip(object):
    def __init__(self, widget, text="widget info"):
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
        label = tk.Label(
            self.tw,
            text=self.text,
            justify="left",
            background="yellow",
            relief="solid",
            borderwidth=1,
            font=("times", "8", "normal"),
        )
        label.pack(ipadx=1)

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()


class Steg:

    global userInput

    def binwalk(self, path):
        cmnd = "binwalk " + path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def exiftool(self, path):
        cmnd = "exiftool " + path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def stegsnow(self, path):
        password = userInput["stegsnow"]
        if password != "":
            cmnd = " -C -p" + password + " " + path
        else:
            cmnd = " -C " + path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        output = process.stdout
        return output

    def steghide(self, path):
        password = userInput["steghide"]
        cmnd = "steghide extract -sf -p" + password + " " + path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def stegseek(self, path):
        wordlistPath = userInput["stegseek"]
        cmnd = "stegseek " + path + " " + wordlistPath
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        print(output)
        return output

    def foremost(self, path):
        outputPath = userInput["foremost"]
        cmnd = "foremost -T " + path + " -o " + outputPath
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def stegoveritas(self, path):
        f = path.split("/")
        out_path = userInput["stegoveritas"]
        cmnd = (
            "stegoveritas  " + path + " -out " + out_path + "/" + f[-1] + "_extracted"
        )
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def xxd(self, path):
        cmnd = "xxd " + path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def zsteg(self, path):
        cmnd = "zsteg -a " + path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def strings(self, path):
        cmnd = "strings " + path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def pngcheck(self, path):
        cmnd = "pngcheck -v " + path
        process = subprocess.run([cmnd], capture_output=True, text=True, shell=True)
        if process.stdout == "":
            output = process.stderr
        else:
            output = process.stdout
        return output

    def jsteg(self, path):
        cmnd = "jsteg reveal " + path
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
        xxdOut = self.xxd(path)
        out = {
            "binwalk": binwalkOut,
            "exiftool": exiftoolOut,
            "strings": stringsOut,
            "pngcheck": pngcheckOut,
            "xxd": xxdOut,
        }

        return out

    def jpgSteg(self, path):
        binwalkOut = self.binwalk(path)
        exiftoolOut = self.exiftool(path)
        stringsOut = self.strings(path)
        xxdOut = self.xxd(path)
        jstegOut = self.jsteg(path)
        out = {
            "binwalk": binwalkOut,
            "exiftool": exiftoolOut,
            "strings": stringsOut,
            "xxd": xxdOut,
            "jsteg": jstegOut,
        }

        return out

    def txtSteg(self, path):
        stegsnowOut = self.stegsnow(path)

        out = {"stegsnow": stegsnowOut}

        return out

    def imageSteg(self, path):
        binwalkOut = self.binwalk(path)
        exiftoolOut = self.exiftool(path)
        stringsOut = self.strings(path)
        pngcheckOut = self.pngcheck(path)
        out = {
            "binwalk": binwalkOut,
            "exiftool": exiftoolOut,
            "strings": stringsOut,
            "pngcheck": pngcheckOut,
        }

        return out

    def audioSteg(self, path):
        binwalkOut = self.binwalk(path)
        exiftoolOut = self.exiftool(path)
        stringsOut = self.strings(path)
        xxdOut = self.xxd(path)
        out = {
            "binwalk": binwalkOut,
            "exiftool": exiftoolOut,
            "strings": stringsOut,
            "xxd": xxdOut,
        }

        return out

    def genericSteg(self, path):
        binwalkOut = self.binwalk(path)
        exiftoolOut = self.exiftool(path)
        stringsOut = self.strings(path)
        xxdOut = self.xxd(path)
        out = {
            "binwalk": binwalkOut,
            "exiftool": exiftoolOut,
            "strings": stringsOut,
            "xxd": xxdOut,
        }

        return out


class UI:
    colours = ["#1E2233", "#36827F", "#F9DB6D"]

    def __init__(self):
        self.window = TkinterDnD.Tk()
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
            self.window.filename = filedialog.askopenfilename(
                initialdir="Documents",
                title="Select file",
                filetypes=[("Select any file", "*")],
            )
            listb.insert("end", self.window.filename)

        def nextUI():
            try:
                inpFilePath = (
                    '"' + listb.get(listb.curselection()).rstrip("}").lstrip("{") + '"'
                )
                destroy()
                extension = inpFilePath.split(".")[-1].rstrip('"')
                if extension == "txt":
                    self.inputUI(inpFilePath, ["stegsnow"])
                else:
                    self.outputUI(inpFilePath)
            except Exception as err:
                debug(err)

        listb = tk.Listbox(
            self.window,
            selectmode=tk.SINGLE,
            bg=self.colours[0],
            fg=self.colours[2],
            font=("Roboto", 10, "bold"),
            height=23,
            width=55,
            borderwidth=5,
        )

        def clear():
            selection = listb.curselection()
            try:
                listb.delete(selection)
            except:
                pass

        def clearAll():
            list_size = listb.size()
            listb.delete(0, list_size)

        banner_label = tk.Label(
            self.window,
            text="STEGALLOFIT",
            font=("Roboto", 30, "bold"),
            bg=self.colours[0],
            fg=self.colours[2],
        )
        widgets.append(banner_label)
        banner_label.place(x=150, y=10)

        choose_file_button = tk.Button(
            self.window,
            command=lambda: choose_file(),
            text="CHOOSE FILE",
            font=("Roboto", 10, "bold"),
            bg=self.colours[1],
            activebackground=self.colours[2],
        )
        widgets.append(choose_file_button)
        choose_file_button.place(x=110, y=460)

        clear_button = tk.Button(
            self.window,
            command=lambda: clear(),
            text="CLEAR",
            font=("Roboto", 10, "bold"),
            bg=self.colours[1],
            activebackground=self.colours[2],
        )
        widgets.append(clear_button)
        clear_button.place(x=260, y=460)

        clear_all_button = tk.Button(
            self.window,
            command=lambda: clearAll(),
            text="CLEAR ALL",
            font=("Roboto", 10, "bold"),
            bg=self.colours[1],
            activebackground=self.colours[2],
        )
        widgets.append(clear_all_button)
        clear_all_button.place(x=360, y=460)

        next_button = tk.Button(
            self.window,
            command=lambda: nextUI(),
            height=2,
            width=9,
            bg=self.colours[0],
            fg=self.colours[1],
            activebackground=self.colours[2],
            text="NEXT",
            font=("Roboto", 10, "bold"),
        )
        widgets.append(next_button)
        next_button.place(x=240, y=530)

        DnD_label = tk.Label(
            self.window,
            text="DROP THE FILE",
            font=("Roboto", 8, "bold"),
            bg=self.colours[0],
            fg=self.colours[1],
        )
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

        CreateToolTip(DnD_label, "Drop the files here!")

    def inputUI(self, filePath, reqInputs):
        widgets = []
        inputCount = 0
        global userInput

        def destroy():
            for widget in widgets:
                widget.place_forget()

        def nextUI():
            debug(f"Inputs: {userInput}")
            destroy()
            self.outputUI(filePath)

        def prevUI():
            destroy()
            self.mainUI()

        def refreshLabel():
            inputLabel.config(text=f"INPUT: {reqInputs[inputCount - 1]}")
            inputLabel.update()

        def nextInput():
            nonlocal inputCount
            inp = inputBox.get(1.0, "end-1c")
            userInput[reqInputs[inputCount - 1]] = inp
            inputCount += 1
            inputBox.delete(1.0, END)
            if inputCount == len(reqInputs):
                debug(userInput)
                nextUI()
            # else:
            #     refreshLabel()

        def skipInput():
            nonlocal inputCount
            userInput[reqInputs[inputCount - 1]] = ""
            inputCount += 1
            inputBox.delete(1.0, END)
            if inputCount == len(reqInputs):
                debug(userInput)
                nextUI()
            # else:
            #     refreshLabel()

        inputLabel = tk.Label(
            self.window,
            text=f"INPUT: {reqInputs[0]}",
            font=("Roboto", 23, "bold"),
            bg=self.colours[0],
            fg=self.colours[2],
        )
        widgets.append(inputLabel)
        inputLabel.place(x=120, y=140)

        inputBox = tk.Text(
            self.window,
            bg=self.colours[0],
            fg=self.colours[2],
            bd=2,
            height=5,
            width=60,
            font=("Roboto", 10, "bold"),
            padx=10,
            pady=5,
        )
        widgets.append(inputBox)
        inputBox.place(x=16, y=230)

        skipButton = tk.Button(
            self.window,
            command=lambda: skipInput(),
            height=1,
            width=8,
            bg=self.colours[0],
            fg=self.colours[1],
            activebackground=self.colours[2],
            text="SKIP",
            font=("Roboto", 15, "bold"),
        )
        skipButton.place(x=140, y=390)
        widgets.append(skipButton)

        nextButton = tk.Button(
            self.window,
            command=lambda: nextInput(),
            height=1,
            width=8,
            bg=self.colours[0],
            fg=self.colours[1],
            activebackground=self.colours[2],
            text="NEXT",
            font=("Roboto", 15, "bold"),
        )
        nextButton.place(x=310, y=390)
        widgets.append(nextButton)

        back_button = tk.Button(
            self.window,
            command=lambda: prevUI(),
            height=1,
            width=8,
            bg=self.colours[0],
            fg=self.colours[1],
            activebackground=self.colours[2],
            text="BACK",
            font=("Roboto", 10, "bold"),
        )
        widgets.append(back_button)
        back_button.place(x=20, y=30)

        return userInput

    def outputUI(self, inpFilePath):
        global userInput
        widgets = []

        def destroy():
            for widget in widgets:
                widget.place_forget()

        def nextUI():
            destroy()
            self.mainUI()

        def modifyText(newText):
            outputBox.config(state=NORMAL)
            outputBox.delete(1.0, END)
            outputBox.insert(END, newText)
            outputBox.config(state=DISABLED)

        def classify():
            try:
                steg = Steg()
                if inpFilePath.rstrip('"').endswith(".png"):
                    debug("Input file path: " + inpFilePath + "\n")
                    outData = steg.pngSteg(inpFilePath)
                elif inpFilePath.rstrip('"').endswith(".jpg") or inpFilePath.endswith(
                    ".jpeg"
                ):
                    debug("Input file path: " + inpFilePath + "\n")
                    outData = steg.jpgSteg(inpFilePath)
                elif inpFilePath.rstrip('"').endswith(".txt"):
                    debug("Input file path: " + inpFilePath + "\n")
                    outData = steg.txtSteg(inpFilePath)
                elif inpFilePath.rstrip('"').endswith(".wav") or inpFilePath.endswith(
                    ".mp3"
                ):
                    debug("Input file path: " + inpFilePath + "\n")
                    outData = steg.audioSteg(inpFilePath)
                else:
                    debug("Input file path: " + inpFilePath + "\n")
                    outData = steg.genericSteg(inpFilePath)

                return outData

            except Exception as err:
                debug(err)

        outData = classify()
        outDataKeys = [string.upper() for string in list(outData.keys())]

        def initOut():
            modifyText(list(outData.values())[0])

        def changeTool(*args):
            toolName = selectedTool.get().lower()
            modifyText(outData[toolName])

        outputBox = scrolledtext.ScrolledText(
            self.window,
            state=DISABLED,
            bg=self.colours[0],
            fg=self.colours[2],
            bd=2,
            height=25,
            width=66,
            font=("Roboto", 9, "bold"),
            padx=10,
            pady=5,
        )
        outputBox.vbar.config(
            troughcolor=self.colours[0],
            background=self.colours[1],
            width=14,
            activebackground=self.colours[2],
        )
        widgets.append(outputBox)
        outputBox.place(x=16, y=100)

        selectedTool = StringVar(self.window)
        selectedTool.set(outDataKeys[0])

        dropdownStyle = ttk.Style()

        self.window.option_add("*TCombobox*Listbox*Background", self.colours[0])
        self.window.option_add("*TCombobox*Listbox*Foreground", self.colours[2])
        self.window.option_add("*TCombobox*Listbox*selectBackground", self.colours[1])
        self.window.option_add("*TCombobox*Listbox*selectForeground", self.colours[2])
        dropdownStyle.map("TCombobox", fieldbackground=[("readonly", self.colours[0])])
        dropdownStyle.map("TCombobox", selectbackground=[("readonly", self.colours[0])])
        dropdownStyle.map("TCombobox", selectforeground=[("readonly", self.colours[2])])
        dropdownStyle.map("TCombobox", background=[("readonly", self.colours[0])])
        dropdownStyle.map("TCombobox", foreground=[("readonly", self.colours[2])])

        toolNameDropdown = ttk.Combobox(
            self.window, textvariable=selectedTool, justify="center"
        )
        toolNameDropdown["values"] = outDataKeys
        toolNameDropdown.configure(font=("Roboto", 12, "bold"), state="readonly")
        toolNameDropdown.bind(
            "<<ComboboxSelected>>", lambda e: toolNameDropdown.selection_clear()
        )

        widgets.append(toolNameDropdown)
        toolNameDropdown.place(x=170, y=530)

        selectedTool.trace("w", changeTool)

        initOut()

        back_button = tk.Button(
            self.window,
            command=lambda: nextUI(),
            height=1,
            width=8,
            bg=self.colours[0],
            fg=self.colours[1],
            activebackground=self.colours[2],
            text="BACK",
            font=("Roboto", 10, "bold"),
        )
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
