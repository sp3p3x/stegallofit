import os, subprocess
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tk_functions import CreateToolTip
from tkinterdnd2 import TkinterDnD, DND_FILES

colours=["#2A2F32","#0D8ABF","#02C39A"]

window=TkinterDnD.Tk()
window.geometry("600x600")
window.title("ATTENDANCE MANAGEMENT")
window.configure(bg=colours[0])
window.resizable(height=0, width=0)

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

def main():
    print(banner)

    while True:
        # inpFilePath = str(input('Image path: '))
        inpFilePath = str(tempPath)
        
        if inpFilePath.endswith('.png'):
            print("Input file path: " + inpFilePath + "\n")
            imageSteg(inpFilePath)
            pngSteg(inpFilePath)
        elif inpFilePath.endswith('.jpg') or inpFilePath.endswith('.jpeg'):
            print("Input file path: " + inpFilePath + "\n")
            imageSteg(inpFilePath)
            jpgSteg(inpFilePath)
        elif inpFilePath.endswith('.txt'):
            print("Input file path: " + inpFilePath + "\n")
            txtSteg(inpFilePath)    
        elif inpFilePath.endswith('.wav') or inpFilePath.endswith('.mp3')  or inpFilePath.endswith('.mp3'):
            print("Input file path: " + inpFilePath + "\n")
            audioSteg(inpFilePath)
        else:
            print("Please enter a valid file path!")
            continue

        break


if __name__ == "__main__":
    main()