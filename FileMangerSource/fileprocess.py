import tkinter
import widgets as wdg
import os
import time

class FileProcess:
    
    def __init__(self):

        self.main_path = ''
        self.file_list = []

    def process_entry_path(self):
        self.main_path = wdg.PathEntry.get_entry_path(self)
        return self.main_path

    def get_directory_content(self):
        
        for file in os.listdir (self.main_path):
            # save file's modified time 
            modified_time = time.strftime('%d-%m-%Y %H:%M', time.localtime(os.path.getmtime(self.main_path + "/" + file)))
            # save file's extension
            split_file_name = os.path.splitext(self.main_path + "/" + file)
            file_extension = split_file_name[1]
            # save file's size
            file_size = os.path.getsize(self.main_path + "/" + file)
            # append to the list of file with corresponding information
            self.file_list.append((file, modified_time, file_extension, file_size))
        


