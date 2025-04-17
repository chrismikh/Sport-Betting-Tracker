from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget
from PyQt5.QtCore import Qt
from .pages import HomePage, NewBetPage, BalancePage, StatisticsPage, SettingsPage, HistoryPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sport Betting Tracker")
        self.resize(1300, 800)  # Set initial size
        self.setFixedSize(self.size())  # Lock the window to this size
        self.init_ui()

    def init_ui(self):
        # Create main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Create header
        header_widget = QWidget()
        header_widget.setFixedHeight(80)
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

        # Add stretch between title and buttons
        header_layout.addSpacing(30)

        # Buttons
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
        self.btn_history = QPushButton("History")
        self.btn_settings = QPushButton("Settings")

        for btn in [self.btn_home, self.btn_new_bet, self.btn_balance, self.btn_stats, self.btn_history]:
            btn.setStyleSheet(button_style)
            header_layout.addWidget(btn)

        header_layout.addStretch()

        self.btn_settings.setStyleSheet(button_style)
        header_layout.addWidget(self.btn_settings)

        # Create stacked widget for content
        self.stacked_widget = QStackedWidget()
        
        # Create and add pages
        self.home_page = HomePage()
        self.new_bet_page = NewBetPage()
        self.balance_page = BalancePage()
        self.stats_page = StatisticsPage()
        self.settings_page = SettingsPage()
        self.history_page = HistoryPage()

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.new_bet_page)
        self.stacked_widget.addWidget(self.balance_page)
        self.stacked_widget.addWidget(self.stats_page)
        self.stacked_widget.addWidget(self.settings_page)
        self.stacked_widget.addWidget(self.history_page)

        # Add widgets to main layout
        main_layout.addWidget(header_widget)
        main_layout.addWidget(self.stacked_widget)

        # Set the main widget
        self.setCentralWidget(main_widget)

        # Connect buttons to page switching
        self.btn_home.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.home_page))
        self.btn_new_bet.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.new_bet_page))
        self.btn_balance.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.balance_page))
        self.btn_stats.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.stats_page))
        self.btn_settings.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.settings_page))
        self.btn_history.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.history_page))

        # Set initial page
        self.stacked_widget.setCurrentWidget(self.home_page)
        