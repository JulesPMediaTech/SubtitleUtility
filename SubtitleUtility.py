from tkinter import *
from tkinter import filedialog
from tkmacosx import Button
from pathlib import Path


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('Subtitle Utility')
        self.geometry('500x200')
        self.l1 = Label(
            self, text='Extract and bake .srt files from .mp4 video files', padx=20, pady=20)
        self.open_but = Button(
            self, text='Open Video File', command=self.open_file)
        self.spacer1 = Frame(self, pady=20)

        self.l1.grid(row=0, column=0, columnspan=3)
        self.spacer1.grid(row=1, column=0, columnspan=3)
        self.open_but.grid(row=2, column=1)

    def open_file(self):
        self.file = filedialog.askopenfilename(initialdir=Path.home(),
                                               title="Select file",
                                               filetypes=(
                                                   ("mp4 files", "*.mp4"), ("all files", "*.*"))
                                               )
        print(self.file)


if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()


# Media apps...
# Runway ML -
# Diffusion Bee
