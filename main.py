import os, subprocess

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
    ch = int(input("Type 1 for encryption and 2 for decryption: "))
    newpath = "newfoo.txt"
    if ch == 1:     
        m = input("input string to be concealed: ")
        p = input("input password: ")
        cmd = " -C -m " + '"' + m +'"' + " -p " + '"' + p + '"' + " " + path + " " + newpath
        print(cmd)
    elif ch == 2:
        p = input("input password")
        cmd = " -C -p" + p + " " +  newpath
        print(cmd)
    output = os.system("stegsnow" + cmd)

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
    # print(banner)

    while True:
        # inpFilePath = str(input('Image path: '))
        inpFilePath = str(tempPath)

        if inpFilePath.endswith('.png'):
            imageSteg(inpFilePath)
            pngSteg(inpFilePath)
        elif inpFilePath.endswith('.jpg') or inpFilePath.endswith('.jpeg'):
            imageSteg(inpFilePath)
            jpgSteg(inpFilePath)
        elif inpFilePath.endswith('.txt'):
            txtSteg(inpFilePath)    
        elif inpFilePath.endswith('.wav') or inpFilePath.endswith('.mp3')  or inpFilePath.endswith('.mp3'):
            audioSteg(inpFilePath)
        else:
            print("Please enter a valid file path!")
            continue

        break


if __name__ == "__main__":
    main()