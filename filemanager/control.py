from display import Display
from process import Process

class Control:

    def __init__(self):
        self.gui = Display()
        self.process = Process()

        self.gui.choose_button.bind('<Button-1>', self.handle_entry_button)
        self.gui.sort_button.bind('<Button-1>', self.handle_sort_button)

    def handle_directory_tree_event(self):
        pass

    def handle_entry_button(self, event):
        self.gui.clear_fileview()
        self.path = self.gui.get_entry_text()
        file_list = self.process.list_files(self.path)
        self.gui.display_files(file_list)


    def handle_sort_button(self, event):
        self.gui.clear_fileview()
        options = self.gui.get_sort_option()
        sorted_file_list = self.process.list_sorted_files(options)
        self.gui.display_files(sorted_file_list)


    def start_window(self):
        self.gui.init_display()

    




if __name__ == '__main__':
    file_manager = Control()
    file_manager.start_window()

