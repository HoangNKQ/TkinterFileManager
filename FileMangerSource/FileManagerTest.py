
import tkinter as tk
from tkinter import ttk
import os 
import time

main_path = ''
directory_content = []
sorted_content = []

def display_file_tree():
    # global object
    global file_tree 
    global directory_content
    global path_entry
    global main_path

    # clear all items in treeview and list
    for item in file_tree.get_children():
        file_tree.delete(item)
    directory_content.clear()

    # get main path from entry box
    main_path = path_entry.get()

    for file in os.listdir(main_path):
        # save file's modified time 
        modified_time = time.strftime('%d-%m-%Y %H:%M', time.localtime(os.path.getmtime(main_path + "/" + file)))

        # save file's extension
        split_file_name = os.path.splitext(main_path + "/" + file)
        file_extension = split_file_name[1]

        # save file's size
        file_size = os.path.getsize(main_path + "/" + file)

        # append to the list of file with corresponding information
        directory_content.append((file, modified_time, file_extension, file_size))

    # insert to file treeview
    for file in directory_content:
        file_tree.insert('', tk.END, values=file)

def sort_file():
    #global objects
    global sort_options
    global directory_content
    global sorted_content
    global file_tree

    # clear all items in treeview
    for item in file_tree.get_children():
        file_tree.delete(item)
    
    # creat new list for sorted content
    sorted_content = directory_content.copy()

    # display file tree in different order 
    if sort_options.get() == 'Name':
        sorted_content = sorted(sorted_content, key= lambda x : x[0].lower())
        for file in sorted_content:
            file_tree.insert('', tk.END, values=file)
    
    if sort_options.get() == 'Date':
        sorted_content.sort(key= lambda x : x[1])
        for file in sorted_content:
            file_tree.insert('', tk.END, values=file)
    
    if sort_options.get() == 'Ext':
        sorted_content.sort(key= lambda x : x[2])
        for file in sorted_content:
            file_tree.insert('', tk.END, values=file)

    if sort_options.get() == 'Size':
        sorted_content.sort(key= lambda x : x[3])
        for file in sorted_content:
            file_tree.insert('', tk.END, values=file)
    


def create_widgets(parent):
    # global object
    global file_tree, path_entry
    global entry_text, sort_options

    # Tkinter Variables
    entry_text = tk.StringVar()
    sort_options = tk.StringVar()
    #
    # Create Directory Path Entry
    #
    path_frame = ttk.LabelFrame(parent, text="Entry", padding=(10, 10))
    path_frame.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky='nsew' )
    path_frame.columnconfigure(0, weight = 8)
    path_frame.columnconfigure(1, weight = 1)

    path_entry = ttk.Entry(path_frame, textvariable= entry_text)
    path_entry.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

    path_button = ttk.Button(path_frame, text= 'Enter', command= display_file_tree)
    path_button.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

    #
    # Create Directory TreeView
    #
    directory_tree_frame = ttk.LabelFrame(parent, text="Directory Browser", padding=(10, 10))
    directory_tree_frame.grid(row=0, column=0, rowspan=3, padx= 5, pady= 5, sticky='nsew')
    directory_tree_frame.columnconfigure(0, weight = 1)
    directory_tree_frame.rowconfigure(0, weight = 20)
    directory_tree_frame.rowconfigure(1, weight = 1)

    directory_tree = ttk.Treeview(directory_tree_frame)
    directory_tree.heading('#0', text='Directory Browser', anchor='w')
    directory_tree.grid(row= 0, column=0,  pady=5, sticky='nsew')

    ysb = ttk.Scrollbar(directory_tree_frame, orient='vertical', command=directory_tree.yview)
    xsb = ttk.Scrollbar(directory_tree_frame, orient='horizontal', command=directory_tree.xview)
    ysb.grid(row=0, column=1, sticky="nse")
    xsb.grid(row=0, column=0, sticky="sew")
    directory_tree.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)

    directory_button = ttk.Button(directory_tree_frame, text= 'Choose Directory')
    directory_button.grid(row=1, column=0, padx=5, pady= 5, sticky='ew')

    #
    # Create File TreeView
    #
    file_tree = ttk.Treeview(parent, columns=('#1', '#2', '#3', '#4'), show='headings')
    file_tree.heading('#1', text= 'Name')
    file_tree.heading('#2', text= 'Date Modified')
    file_tree.heading('#3', text= 'File Type')
    file_tree.heading('#4', text= 'Size')
    file_tree.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

    file_sb = ttk.Scrollbar(parent, orient='vertical', command=file_tree.yview)
    file_sb.grid(row=1, column=1, sticky="nse")
    file_tree.configure(yscrollcommand=file_sb.set)

    #
    # Create File Operations 
    #
    file_operation_frame = ttk.LabelFrame(parent, text="File Operation", padding=(10, 10))
    file_operation_frame.grid(row=2, column=1, padx=(20, 10), pady=(20, 10), sticky='nsew' )
    file_operation_frame.columnconfigure(0, weight = 1)
    file_operation_frame.columnconfigure(1, weight = 1)
    file_operation_frame.columnconfigure(2, weight = 1)
    
    copy_button = ttk.Button(file_operation_frame, text='Copy')
    copy_button.grid(row=0, column=0, padx=5, pady= 5, sticky= 'ew')

    paste_button = ttk.Button(file_operation_frame, text='Paste')
    paste_button.grid(row=0, column=1, padx=5, pady= 5, sticky= 'ew')

    cut_button = ttk.Button(file_operation_frame, text='Cut')
    cut_button.grid(row=0, column=2, padx=5, pady= 5, sticky= 'ew')

    #
    # Create Sorting Options
    #
    file_sorting_frame = ttk.LabelFrame(parent, text="Sorting Options", padding=(10, 10))
    file_sorting_frame.grid(row=1, column=2, padx=(20, 10), pady=(20, 10), sticky='nsew')
    file_sorting_frame.columnconfigure(0, weight = 1)
    file_sorting_frame.columnconfigure(1, weight = 1)
    file_sorting_frame.rowconfigure(0, weight = 2)
    file_sorting_frame.rowconfigure(1, weight = 2)
    file_sorting_frame.rowconfigure(2, weight = 2)
    file_sorting_frame.rowconfigure(3, weight = 2)
    file_sorting_frame.rowconfigure(4, weight = 1)

    option_1 = ttk.Radiobutton(file_sorting_frame, text='By Name', value='Name', variable= sort_options)
    option_1.grid(row=0, column=0, columnspan=2, sticky='w')
    option_2 = ttk.Radiobutton(file_sorting_frame, text='By Modified Date', value='Date', variable= sort_options)
    option_2.grid(row=1, column=0, columnspan=2, sticky='w')
    option_3 = ttk.Radiobutton(file_sorting_frame, text='By Extension', value='Ext', variable= sort_options)
    option_3.grid(row=2, column=0, columnspan=2, sticky='w')
    option_4 = ttk.Radiobutton(file_sorting_frame, text='By Size', value='Size', variable= sort_options)
    option_4.grid(row=3, column=0, columnspan=2, sticky='w')
    
    sort_button = ttk.Button(file_sorting_frame, text='Sort', command= sort_file)
    sort_button.grid(row = 4, column=1, padx= 5, pady= 5, sticky='ew')
    # undo_button = ttk.Button(file_sorting_frame, text='Undo', command= )
    # undo_button.grid(row = 4, column=0, padx= 5, pady= 5, sticky='ew')


def main():
    root = tk.Tk()
    root.title('File Manager')
    root.tk.call("source", "TkinterFileManager\FileMangerSource\sun-valley.tcl")
    root.tk.call("set_theme", "dark")

    # Grid Manager
    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight = 5)
    root.columnconfigure(2, weight = 1)
    root.rowconfigure(0, weight = 1)
    root.rowconfigure(1, weight = 20)
    root.rowconfigure(2, weight = 1)

    # Creating All Widgets
    create_widgets(root)

    root.mainloop()

if __name__ == "__main__":
    main()