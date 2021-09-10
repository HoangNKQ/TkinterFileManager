import tkinter as tk
import widgets as wdg

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FILE MANAGER")
        self.tk.call("source", "FileMangerSource\sun-valley.tcl")
        self.tk.call("set_theme", "dark")

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 5)
        self.columnconfigure(2, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 20)
        self.rowconfigure(2, weight = 1)

        self.create_frame()

    def create_frame(self):
        entry_frame = wdg.PathEntry(self)
        entry_frame.grid (row=0, column=1, padx= 5, pady= 5, sticky= 'ew')

        file_frame = wdg.FileView(self)
        file_frame.grid (row=1, column=1, padx=5, pady=5, sticky='nsew')

        directory_frame = wdg.DirectoryView(self)
        directory_frame.grid (row=0, column=0, rowspan= 3, padx=5, pady=5, sticky='nsew')

        sort_option_frame = wdg.SortOptions(self)
        sort_option_frame.grid (row= 1, column=2, padx= 5, pady= 5, sticky= 'nsew')

        operation_frame = wdg.FileOperation(self)
        operation_frame.grid (row= 2, column= 1, padx= 5, pady= 5, sticky='nsew')

if __name__ == '__main__':
    app = MainApp()
    app.mainloop()