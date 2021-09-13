from display import Display
from process import Process

class Control:
    def __init__(self):
        self.display = Display()
        self.process = Process()

    def start_window(self):
        self.display.init_display()




if __name__ == '__main__':
    file_manager = Control()
    file_manager.start_window()

