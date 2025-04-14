from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sport Betting Tracker")
        self.resize(1300, 800)  # Set initial size
        self.setFixedSize(self.size())  # Lock the window to this size
        self.init_ui()

    # Header for the main window
    def init_ui(self):
        # Create a QWidget to act as the header container
        header_widget = QWidget(self)
        header_widget.setGeometry(0, 0, 1300, 80)
        header_widget.setStyleSheet("background-color: #1e1e1e;")

        # Create layout for the header
        header_layout = QHBoxLayout(header_widget)
        header_layout.setContentsMargins(20, 10, 20, 10)
        header_layout.setSpacing(15)

        # Left-aligned label
        title_label = QLabel("Betting Tracker")
        title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 28px;
                font-weight: bold;
            }
        """)
        header_layout.addWidget(title_label)

        # Add stretch between title and buttons to push buttons to the right
        header_layout.addSpacing(30)

    # Buttons (inline)
        button_style = """
            QPushButton {
                background-color: #2a2a2a;
                color: white;
                border: none;
                padding: 8px 16px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #3a3a3a;
            }
        """

        self.btn_home = QPushButton("Home")
        self.btn_new_bet = QPushButton("New Bet")
        self.btn_balance = QPushButton("Balance")
        self.btn_stats = QPushButton("Statistics")
        self.btn_settings = QPushButton("Settings")

        for btn in [self.btn_home, self.btn_new_bet, self.btn_balance, self.btn_stats]:
            btn.setStyleSheet(button_style)
            header_layout.addWidget(btn)

        header_layout.addStretch()  # Push the settings button to the far right

        self.btn_settings.setStyleSheet(button_style)
        header_layout.addWidget(self.btn_settings)
        