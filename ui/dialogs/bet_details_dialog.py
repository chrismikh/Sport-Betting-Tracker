from PyQt5.QtWidgets import (QDialog, QLabel, QVBoxLayout, QHBoxLayout,
                            QPushButton, QFrame, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from typing import Dict, Any, Optional
from ..utils.formatters import Formatters

class BetDetailsDialog(QDialog):
    def __init__(self, bet_details: Dict[str, Any], parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Bet Details")
        self.setFixedSize(500, 400)
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {Formatters.COLOR_BACKGROUND};
                color: {Formatters.COLOR_TEXT};
            }}
            QLabel {{
                color: {Formatters.COLOR_TEXT};
                font-size: 14px;
                padding: 5px;
            }}
            QPushButton {{
                background-color: {Formatters.COLOR_BORDER};
                color: {Formatters.COLOR_TEXT};
                border: none;
                padding: 8px;
                border-radius: 5px;
                min-width: 100px;
            }}
            QPushButton:hover {{
                background-color: #4a4a4a;
            }}
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title_label = QLabel("Bet Details")
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet(f"background-color: {Formatters.COLOR_BORDER};")
        layout.addWidget(separator)
        
        # Bet details
        details_layout = QVBoxLayout()
        details_layout.setSpacing(5)
        
        # Format and display each detail
        for key, value in bet_details.items():
            if key == 'result':
                result_color = Formatters.get_result_color(value)
                result_label = QLabel(f"Result: {value}")
                result_label.setStyleSheet(f"color: {result_color}; font-weight: bold;")
                details_layout.addWidget(result_label)
            elif key == 'profit_loss':
                pl_value = float(value)
                pl_text = Formatters.format_profit_loss(pl_value)
                pl_label = QLabel(f"Profit/Loss: {pl_text}")
                pl_label.setStyleSheet(f"color: {Formatters.get_profit_loss_color(pl_value)}; font-weight: bold;")
                details_layout.addWidget(pl_label)
            elif key == 'amount':
                # Format amount with currency
                amount_text = Formatters.format_currency(float(value))
                details_layout.addWidget(QLabel(f"Amount: {amount_text}"))
            elif key == 'odds':
                # Format odds
                odds_text = Formatters.format_odds(value)
                details_layout.addWidget(QLabel(f"Odds: {odds_text}"))
            elif key == 'date':
                # Format date
                date_text = Formatters.format_date(value)
                details_layout.addWidget(QLabel(f"Date: {date_text}"))
            else:
                # Format the key for display
                display_key = key.replace('_', ' ').title()
                details_layout.addWidget(QLabel(f"{display_key}: {value}"))
        
        layout.addLayout(details_layout)
        
        # Add some space
        layout.addStretch()
        
        # Close button
        button_layout = QHBoxLayout()
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout) 