from PyPDF2 import PdfMerger
from tkinter import *
from tkinter import filedialog
import os.path

FILES_TO_MERGE = None
OUT_PATH = None





### GUI logic ----------------------------------------------------------


# Widgets - Select Files to Merge
def select_in():
    """Store user-selected files to merge as global FILES_TO_MERGE"""
    global FILES_TO_MERGE
    FILES_TO_MERGE = list(filedialog.askopenfilenames(filetypes=[("PDF",('*.pdf'))]))


# Widgets - Select Output Directory
def select_out():
    """Store user-selected output directory as OUT_PATH"""
    global OUT_PATH
    OUT_PATH = filedialog.askdirectory(title="Choose output directory")


# Widgets - Merge Button
def merge():
    """Begin merge logic"""
    merger = PdfMerger()
    
    for pdf in FILES_TO_MERGE:
        merger.append(pdf)
        
    merger.write(os.path.join(OUT_PATH, "merged.pdf"))
    merger.close()    





### GUI Structure ------------------------------------------------------


def create_label_frame(container):
    frame = Frame(container)
    Label(frame, text="Selected files:").grid(column=0, row=0, sticky=W)
    Label(frame, text="Selected destination:").grid(column=0, row=1, sticky=W)
    Label(frame, text='').grid(column=0, row=2) # Spacer
    
    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)
    
    return frame


def create_button_frame(container):
    frame = Frame(container)
    
    Button(frame, text="Select", command=select_in).grid(column=0, row=0, sticky=E)
    Button(frame, text="Select", command=select_out).grid(column=0, row=1, sticky=E)
    Button(frame, text="Merge", command=merge).grid(column=0, row=2, sticky=E)
    
    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)    
    
    return frame
    
    
def create_main_window():
    # Create root window
    root = Tk()
    root.title("Basic PDF Merger")
    root.geometry('200x150') # Width x height of root window
    
    # Layout on the root window
    root.columnconfigure(0, weight=2)
    root.columnconfigure(1, weight=1)
    label_frame = create_label_frame(root)
    label_frame.grid(column=0, row=0)
    button_frame = create_button_frame(root)
    button_frame.grid(column=2, row=0)
    
    root.mainloop()
    


    
    
### Main loop ---------------------------------------------------------
    
if __name__ == "__main__":
    create_main_window()