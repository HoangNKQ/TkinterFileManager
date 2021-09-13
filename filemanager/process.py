import os
import time

class Process:
    
    files = []

    def list_files(self, main_path):
        for file in os.listdir(main_path):
            # save file's modified time 
            modified_time = time.strftime('%d-%m-%Y %H:%M', time.localtime(os.path.getmtime(main_path + "/" + file)))
            # save file's extension
            split_file_name = os.path.splitext(main_path + "/" + file)
            file_extension = split_file_name[1]
            # save file's size
            file_size = os.path.getsize(main_path + "/" + file)
            # append to the list of file with corresponding information
            self.files.append((file, modified_time, file_extension, file_size))

        return self.files

    