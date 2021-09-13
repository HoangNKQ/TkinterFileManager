from display import Display
from process import Process

class Control:

    def __init__(self):
        self.gui = Display()
        self.process = Process()

        self.gui.choose_button.bind('<Button-1>', self.handle_entry_button)

    def handle_entry_button(self, event):
        self.path = self.gui.get_entry_text()
        print (self.path)

    def handle_sort_button(self):
        pass

    def start_window(self):
        self.gui.init_display()

    




if __name__ == '__main__':
    file_manager = Control()
    file_manager.start_window()

