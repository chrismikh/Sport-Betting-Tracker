from PyQt5.QtWidgets import QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sport Betting Tracker")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        label = QLabel("Welcome to your Betting Tracker!", self)
        label.move(20, 20)
