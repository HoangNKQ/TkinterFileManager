import tkinter as tk
from tkinter import ttk

class Display(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FILE MANAGER")
        self.tk.call("source", "theme\sun-valley.tcl")
        self.tk.call("set_theme", "dark")

        self.setup_frame()
        self.init_frame()

    def setup_frame(self):
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 5)
        self.columnconfigure(2, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 20)
        self.rowconfigure(2, weight = 1)

    def init_frame(self):
        entry_frame = PathEntry(self)
        entry_frame.grid (row=0, column=1, padx= 5, pady= 5, sticky= 'ew')

        file_frame = FileView(self)
        file_frame.grid (row=1, column=1, padx=5, pady=5, sticky='nsew')

        directory_frame = DirectoryView(self)
        directory_frame.grid (row=0, column=0, rowspan= 3, padx=5, pady=5, sticky='nsew')

        sort_option_frame = SortOptions(self)
        sort_option_frame.grid (row= 1, column=2, padx= 5, pady= 5, sticky= 'nsew')

        operation_frame = FileOperation(self)
        operation_frame.grid (row= 2, column= 1, padx= 5, pady= 5, sticky='nsew')

    def init_display(self):
        self.mainloop()



class PathEntry(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.path_text = tk.StringVar()

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        self.widget_init()

    def widget_init(self):
        entry_label = ttk.LabelFrame(self, text= "Directory Path", padding=(5, 5))
        entry_label.grid(row= 0, column=0, padx= 5, pady= 5, sticky= 'we')
        entry_label.rowconfigure (0, weight = 1)
        entry_label.columnconfigure (0, weight = 10)
        entry_label.columnconfigure (1, weight = 1)

        entry_box = ttk.Entry(entry_label, textvariable= self.path_text)
        entry_box.grid(row= 0 ,column= 0, padx = 5, pady= 5, sticky='we')

        choose_button = ttk.Button(entry_label, text= 'Enter')
        choose_button.grid(row= 0, column= 1, pady=5, padx= 5, sticky='we')

    def get_text_entry(self):
        return self.path_text.get()

    def set_text_entry(self, text):
        self.path_text.set(text)



class FileView(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        self.widget_init()

    def widget_init(self):
        self.file_tree = ttk.Treeview(self, columns=('#1', '#2', '#3', '#4'), show='headings')
        self.file_tree.heading('#1', text= 'Name')
        self.file_tree.heading('#2', text= 'Date Modified')
        self.file_tree.heading('#3', text= 'File Type')
        self.file_tree.heading('#4', text= 'Size')
        self.file_tree.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        file_sb = ttk.Scrollbar(self, orient='vertical', command=self.file_tree.yview)
        file_sb.grid(row=0, column=0, sticky="nse")
        self.file_tree.configure(yscrollcommand=file_sb.set)



class DirectoryView(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        self.widget_init()

    def widget_init(self):
        directory_tree_frame = ttk.LabelFrame(self, text="Directory Browser", padding=(10, 10))
        directory_tree_frame.grid(row=0, column=0, padx= 5, pady= 5, sticky='nsew')
        directory_tree_frame.columnconfigure(0, weight = 1)
        directory_tree_frame.rowconfigure(0, weight = 20)
        directory_tree_frame.rowconfigure(1, weight = 1)

        self.directory_tree = ttk.Treeview(directory_tree_frame)
        self.directory_tree.heading('#0', text='Directory Browser', anchor='w')
        self.directory_tree.grid(row= 0, column=0,  pady=5, sticky='nsew')

        ysb = ttk.Scrollbar(directory_tree_frame, orient='vertical', command=self.directory_tree.yview)
        xsb = ttk.Scrollbar(directory_tree_frame, orient='horizontal', command=self.directory_tree.xview)
        ysb.grid(row=0, column=1, sticky="nse")
        xsb.grid(row=0, column=0, sticky="sew")
        self.directory_tree.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)



class SortOptions(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.sort_option = tk.StringVar()

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        self.widget_init()

    def widget_init(self):
        file_sorting_frame = ttk.LabelFrame(self, text="Sorting Options", padding=(5, 5))
        file_sorting_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky='nsew')
        file_sorting_frame.columnconfigure(0, weight = 1)
        file_sorting_frame.columnconfigure(1, weight = 1)
        file_sorting_frame.rowconfigure(0, weight = 2)
        file_sorting_frame.rowconfigure(1, weight = 2)
        file_sorting_frame.rowconfigure(2, weight = 2)
        file_sorting_frame.rowconfigure(3, weight = 2)
        file_sorting_frame.rowconfigure(4, weight = 1)

        option_1 = ttk.Radiobutton(file_sorting_frame, text='By Name', value='Name', variable= self.sort_option)
        option_1.grid(row=0, column=0, columnspan=2, sticky='w')
        option_2 = ttk.Radiobutton(file_sorting_frame, text='By Modified Date', value='Date', variable= self.sort_option)
        option_2.grid(row=1, column=0, columnspan=2, sticky='w')
        option_3 = ttk.Radiobutton(file_sorting_frame, text='By Extension', value='Ext', variable= self.sort_option)
        option_3.grid(row=2, column=0, columnspan=2, sticky='w')
        option_4 = ttk.Radiobutton(file_sorting_frame, text='By Size', value='Size', variable= self.sort_option)
        option_4.grid(row=3, column=0, columnspan=2, sticky='w')

        sort_button = ttk.Button(file_sorting_frame, text='Sort')
        sort_button.grid(row = 4, column=1, padx= 5, pady= 5, sticky='ew')

    def get_sort_option(self):
        return self.sort_option.get()



class FileOperation(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        self.widget_init()

    def widget_init(self):
        file_operation_frame = ttk.LabelFrame(self, text="File Operation", padding=(5, 5))
        file_operation_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky='nsew' )
        file_operation_frame.columnconfigure(0, weight = 1)
        file_operation_frame.columnconfigure(1, weight = 1)
        file_operation_frame.columnconfigure(2, weight = 1)
        
        copy_button = ttk.Button(file_operation_frame, text='Copy')
        copy_button.grid(row=0, column=0, padx=5, pady= 5, sticky= 'ew')

        paste_button = ttk.Button(file_operation_frame, text='Paste')
        paste_button.grid(row=0, column=1, padx=5, pady= 5, sticky= 'ew')

        cut_button = ttk.Button(file_operation_frame, text='Cut')
        cut_button.grid(row=0, column=2, padx=5, pady= 5, sticky= 'ew')
