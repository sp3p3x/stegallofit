import os, subprocess

tempPath = "foo.png"

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
    output = os.system("binwalk " + path)
    print(output)

def pngSteg(path):
    pass

def jpgSteg(path):
    pass

def imageSteg(path):
    binwalk(path)

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
        elif inpFilePath.endswith('.wav') or inpFilePath.endswith('.mp3')  or inpFilePath.endswith('.mp3'):
            audioSteg(inpFilePath)
        else:
            print("Please enter a valid file path!")
            continue

        break


if __name__ == "__main__":
    main()