from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


Folder_Name = ""

# File Location

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        pathError.config(text=Folder_Name, fg="green")
    else:
        pathError.config(text="Please Choose Folder !!", fg="red")


# Download Video Quality

def DownloadVideo():
    choice = ydChoices.get()
    url = ydEntry.get()

    if(len(url) > 1):
        ydError.config(text="")
        yd = YouTube(url)

        if(choice == choices[0]):
            select = yd.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yd.streams.filter(progressive=True, file_extension="mp4").last()

        elif(choice == choices[2]):
            select = yd.streams.filter(only_audio=True).first()

        else:
            ydError.config(text="Please Check the Link !!", fg="red")

    # Download function
    select.download(Folder_Name)
    ydError.config(text="Download Completed !!", fg="green")


root = Tk()
root.geometry('350x400')    # Set window
root.columnconfigure(0, weight=1)    # set all content to center
root.title("YouTube Video Downloader")


# YD Link Label
ydLabel = Label(root, text="Enter Your URL: ", font=("Jost", 15))
ydLabel.grid()

# YD Entry Box
ydEntryVar = StringVar()
ydEntry = Entry(root, width=50, textvariable=ydEntryVar)
ydEntry.grid()

# Error Message
ydError = Label(root, text="URL doesn't match", fg="red", font=("jost", 10))
ydError.grid(pady=10)

# Save File
saveLabel = Label(root, text="Choose File Path", font=("jost", 15))
saveLabel.grid()

# Button For Choose Path
saveEntry = Button(root, text="Choose Path", bg="red", fg="white", width=15,command=openLocation)
saveEntry.grid()

# Path Error
pathError = Label(root, text="Path doesn't match", fg="red", font=("jost", 10))
pathError.grid(pady=10)

# Quality Label
qualityLabel = Label(root, text="Select Quality", font=("jost", 15))
qualityLabel.grid()

# Combobox
choices = ['720p', '480p', '360p', '144', 'mp3']
ydChoices = ttk.Combobox(root, values = choices)
ydChoices.grid()

# Download Buttons
downloadBtn = Button(root, width=10, text="Download", bg="red", fg="white", command=DownloadVideo)
downloadBtn.grid(pady=5)


root.mainloop()
