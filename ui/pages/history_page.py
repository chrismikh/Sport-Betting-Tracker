from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class HistoryPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Bet History Page")
        label.setStyleSheet("font-size: 24px;")
        layout.addWidget(label)
        self.setLayout(layout) 