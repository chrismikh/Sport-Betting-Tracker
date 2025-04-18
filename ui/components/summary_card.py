from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class SummaryCard(QFrame):
    def __init__(self, title, value, color=None, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QFrame {
                background-color: #2a2a2a;
                border-radius: 10px;
                padding: 10px;
            }
            QLabel {
                color: white;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(5)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Title label
        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("font-size: 16px; color: #888888;")
        
        # Value label
        self.value_label = QLabel(str(value))
        self.value_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        # Set color if provided
        if color:
            self.set_value_color(color)
        
        layout.addWidget(self.title_label)
        layout.addWidget(self.value_label)
        
        self.setLayout(layout)
        
    def update_value(self, value, highlight=None):
        """Update the value displayed in the card and optionally highlight specific parts
        
        Args:
            value: The new value to display
            highlight: Dictionary of {color: value} pairs to highlight specific parts
                      Example: {'green': 5, 'red': 3} will highlight 5 in green and 3 in red
        """
        if highlight:
            # If we have specific parts to highlight
            current_text = str(value)
            for color, val in highlight.items():
                if color == 'green':
                    colored_text = current_text.replace(str(val), f'<span style="color: #4CAF50;">{val}</span>')
                elif color == 'red':
                    colored_text = current_text.replace(str(val), f'<span style="color: #F44336;">{val}</span>')
                current_text = colored_text
            self.value_label.setText(current_text)
            self.value_label.setTextFormat(Qt.RichText)
        else:
            # If we're just updating the value
            self.value_label.setText(str(value))
            self.value_label.setTextFormat(Qt.PlainText)
            
    def set_value_color(self, color):
        """Set the color of the entire value label"""
        if color == 'green':
            self.value_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #4CAF50;")
        elif color == 'red':
            self.value_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #F44336;")
        else:
            self.value_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;") 