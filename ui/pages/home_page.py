from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout, 
                            QTableWidget, QTableWidgetItem, QHeaderView,
                            QPushButton)
from PyQt5.QtCore import Qt, pyqtSignal, QDateTime
from PyQt5.QtGui import QFont, QColor
from typing import List, Dict, Any, Optional
from ..components.summary_card import SummaryCard
from ..dialogs.bet_details_dialog import BetDetailsDialog
from ..utils.formatters import Formatters

class HomePage(QWidget):
    # Define signals
    new_bet_clicked = pyqtSignal()
    statistics_clicked = pyqtSignal()
    balance_clicked = pyqtSignal()
    history_clicked = pyqtSignal()
    bet_details_clicked = pyqtSignal(dict)  # Signal for bet details, emits bet data
    
    # Color constants
    COLOR_GREEN = "#4CAF50"
    COLOR_RED = "#F44336"
    COLOR_YELLOW = "#FFC107"
    COLOR_GRAY = "#888888"
    COLOR_TEXT = "#ffffff"
    COLOR_ROW_HOVER = "#3a3a3a"
    COLOR_DEFAULT_ROW = "#2a2a2a"
    COLOR_BACKGROUND = "#2a2a2a"
    COLOR_GRIDLINE = "#3a3a3a"
    COLOR_HEADER = "#1e1e1e"
    
    # Card labels as class variable
    CARD_LABELS = {
        'total_bets': "Total Bets",
        'wins_losses': "Wins / Losses",
        'profit_loss': "Total Profit/Loss",
        'active_bets': "Active Bets"
    }
    
    # Table headers as class variable
    TABLE_HEADERS = ["Match", "Date", "Amount", "Odds", "Result", "Profit/Loss"]
    
    # Button style as class variable
    button_style = """
        QPushButton {
            background-color: #2a2a2a;
            color: white;
            border: none;
            padding: 15px;
            font-size: 16px;
            border-radius: 10px;
            min-width: 200px;
        }
        QPushButton:hover {
            background-color: #3a3a3a;
        }
    """
    
    def __init__(self) -> None:
        super().__init__()
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Welcome title
        title_label = QLabel("Welcome Back!")
        title_font = QFont()
        title_font.setPointSize(32)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: white;")
        main_layout.addWidget(title_label)
        
        # Summary cards grid
        cards_layout = QGridLayout()
        cards_layout.setSpacing(15)
        cards_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create summary cards
        self.total_bets_card = SummaryCard(self.CARD_LABELS['total_bets'], "0")
        self.wins_losses_card = SummaryCard(self.CARD_LABELS['wins_losses'], "0 / 0")
        self.profit_loss_card = SummaryCard(self.CARD_LABELS['profit_loss'], "$0.00")
        self.active_bets_card = SummaryCard(self.CARD_LABELS['active_bets'], "0")
        
        # Add cards to grid
        cards_layout.addWidget(self.total_bets_card, 0, 0)
        cards_layout.addWidget(self.wins_losses_card, 0, 1)
        cards_layout.addWidget(self.profit_loss_card, 0, 2)
        cards_layout.addWidget(self.active_bets_card, 0, 3)
        
        # Add cards layout to main layout
        main_layout.addLayout(cards_layout)
        
        # Recent Activity Section
        recent_activity_label = QLabel("Recent Activity")
        activity_font = QFont()
        activity_font.setPointSize(24)
        activity_font.setBold(True)
        recent_activity_label.setFont(activity_font)
        recent_activity_label.setStyleSheet("color: white;")
        main_layout.addWidget(recent_activity_label)
        
        # Create table for recent bets
        self.recent_bets_table = QTableWidget()
        self.recent_bets_table.setObjectName("recentBetsTable")
        self.recent_bets_table.setColumnCount(len(self.TABLE_HEADERS))
        self.recent_bets_table.setHorizontalHeaderLabels(self.TABLE_HEADERS)
        
        # Style the table
        self.recent_bets_table.setStyleSheet(f"""
            QTableWidget {{
                background-color: {self.COLOR_BACKGROUND};
                color: {self.COLOR_TEXT};
                border: none;
                border-radius: 10px;
                gridline-color: {self.COLOR_GRIDLINE};
            }}
            QHeaderView::section {{
                background-color: {self.COLOR_HEADER};
                color: {self.COLOR_TEXT};
                padding: 8px;
                border: none;
                font-weight: bold;
            }}
            QTableWidget::item {{
                padding: 8px;
            }}
        """)
        
        # Set table properties
        self.recent_bets_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.recent_bets_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.recent_bets_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.recent_bets_table.setSelectionMode(QTableWidget.NoSelection)
        self.recent_bets_table.setShowGrid(True)
        self.recent_bets_table.verticalHeader().setVisible(False)
        self.recent_bets_table.setSortingEnabled(True)  # Enable sorting
        
        # Disable focus and selection highlighting
        self.recent_bets_table.setFocusPolicy(Qt.NoFocus)

        # Connect hover events
        self.recent_bets_table.entered.connect(lambda index: self._handle_row_hover(index.row()))
        self.recent_bets_table.viewport().setMouseTracking(True)
        self.recent_bets_table.leaveEvent = self._handle_leave_event
        self.recent_bets_table.mouseMoveEvent = self._handle_mouse_move
        
        # Connect double-click signal
        self.recent_bets_table.cellDoubleClicked.connect(self.handle_bet_details)
        
        # Set fixed height for the table
        self.recent_bets_table.setFixedHeight(200)
        
        main_layout.addWidget(self.recent_bets_table)
        
        # Add some space before Quick Actions
        main_layout.addSpacing(20)
        
        # Quick Actions Section
        quick_actions_label = QLabel("Quick Actions")
        quick_actions_label.setFont(activity_font)
        quick_actions_label.setStyleSheet("color: white;")
        main_layout.addWidget(quick_actions_label)
        
        # Create quick actions grid
        quick_actions_grid = QGridLayout()
        quick_actions_grid.setSpacing(15)
        quick_actions_grid.setContentsMargins(0, 0, 0, 0)
        
        # Create quick action buttons using helper method
        self.btn_new_bet = self.create_button("New Bet", "btnNewBet", "Record a new bet")
        self.btn_statistics = self.create_button("Statistics", "btnStatistics", "View betting statistics")
        self.btn_balance = self.create_button("Check Balance", "btnBalance", "Check your current balance")
        self.btn_history = self.create_button("View All Bets", "btnHistory", "View your complete betting history")
        
        # Add buttons to grid
        quick_actions_grid.addWidget(self.btn_new_bet, 0, 0)
        quick_actions_grid.addWidget(self.btn_statistics, 0, 1)
        quick_actions_grid.addWidget(self.btn_balance, 1, 0)
        quick_actions_grid.addWidget(self.btn_history, 1, 1)
        
        # Add quick actions grid to main layout
        main_layout.addLayout(quick_actions_grid)
        
        self.setLayout(main_layout)
        
        # Connect button signals
        self.btn_new_bet.clicked.connect(self.handle_new_bet)
        self.btn_statistics.clicked.connect(self.handle_statistics)
        self.btn_balance.clicked.connect(self.handle_balance)
        self.btn_history.clicked.connect(self.handle_history)
        
        # Store the current bets data for quick access
        self._current_bets: List[Dict[str, Any]] = []
        
    def create_button(self, text, object_name, tooltip):
        """Helper method to create styled buttons with object name and tooltip"""
        btn = QPushButton(text)
        btn.setStyleSheet(self.button_style)
        btn.setObjectName(object_name)
        btn.setToolTip(tooltip)
        return btn
        
    def handle_new_bet(self):
        """Handle new bet button click"""
        self.new_bet_clicked.emit()
        
    def handle_statistics(self):
        """Handle statistics button click"""
        self.statistics_clicked.emit()
        
    def handle_balance(self):
        """Handle balance button click"""
        self.balance_clicked.emit()
        
    def handle_history(self):
        """Handle history button click"""
        self.history_clicked.emit()
        
    def get_bet_data(self, row: int) -> Optional[Dict[str, Any]]:
        """Get bet details for a specific row"""
        if not self._current_bets or not 0 <= row < len(self._current_bets):
            return None
        return self._current_bets[row]

    def handle_bet_details(self, row: int, column: int) -> None:
        """Handle bet details double-click"""
        bet_data = self.get_bet_data(row)
        if bet_data:
            dialog = BetDetailsDialog(bet_data, self)
            dialog.exec_()
            # Emit signal for potential parent updates
            self.bet_details_clicked.emit(bet_data)
        
    def update_stats(self, total_bets, wins, losses, profit_loss, active_bets):
        """Update the summary cards with new values"""
        self.total_bets_card.update_value(str(total_bets))
        
        # Update wins/losses with colors using the new highlight feature
        wins_losses_text = f"{wins} / {losses}"
        self.wins_losses_card.update_value(wins_losses_text, highlight={'green': wins, 'red': losses})
        
        # Update profit/loss with improved formatting
        pl_value = f"${abs(profit_loss):.2f}"
        if profit_loss > 0:
            pl_value = f"+{pl_value}"
            self.profit_loss_card.update_value(pl_value, highlight={'green': pl_value})
        elif profit_loss < 0:
            pl_value = f"–{pl_value}"
            self.profit_loss_card.update_value(pl_value, highlight={'red': pl_value})
        else:
            self.profit_loss_card.update_value(pl_value)
        
        self.active_bets_card.update_value(str(active_bets))
        
    def _get_profit_loss_color(self, value):
        """Returns the color based on profit or loss value."""
        if value > 0:
            return self.COLOR_GREEN
        elif value < 0:
            return self.COLOR_RED
        return self.COLOR_TEXT

    def _get_result_color(self, result):
        """Returns the color based on bet result."""
        result = result.lower() if result else ''
        if result == 'won':
            return self.COLOR_GREEN
        elif result == 'lost':
            return self.COLOR_RED
        return self.COLOR_YELLOW

    def _create_table_item(self, text: str, alignment: int = Qt.AlignCenter, color: str = None) -> QTableWidgetItem:
        """Helper method to create a table item with consistent formatting"""
        item = QTableWidgetItem(text)
        item.setTextAlignment(alignment)
        if color:
            item.setForeground(QColor(color))
        return item

    def _update_table_row(self, row: int, bet: Dict[str, Any]) -> None:
        """Update a single row in the table with bet data"""
        # Match
        match_text = bet.get('match', '—')
        self.recent_bets_table.setItem(row, 0, self._create_table_item(match_text))
        
        # Date
        date = Formatters.format_date(bet.get('date'))
        self.recent_bets_table.setItem(row, 1, self._create_table_item(date))
        
        # Amount
        amount = Formatters.format_currency(bet.get('amount', 0))
        self.recent_bets_table.setItem(row, 2, self._create_table_item(amount))
        
        # Odds
        odds = bet.get('odds')
        odds_text = Formatters.format_odds(odds)
        self.recent_bets_table.setItem(row, 3, self._create_table_item(odds_text))
        
        # Result
        result = bet.get('result', '—')
        result_item = self._create_table_item(result, color=Formatters.get_result_color(result))
        self.recent_bets_table.setItem(row, 4, result_item)
        
        # Profit/Loss
        profit_loss = bet.get('profit_loss', 0)
        pl_value = Formatters.format_profit_loss(profit_loss)
        pl_item = self._create_table_item(pl_value, color=Formatters.get_profit_loss_color(profit_loss))
        self.recent_bets_table.setItem(row, 5, pl_item)

    def update_recent_bets(self, bets: List[Dict[str, Any]]) -> None:
        """Update the recent bets table with new data
        bets: List of dictionaries with keys: match, date, amount, odds, result, profit_loss
        """
        # Store the current bets for quick access
        self._current_bets = bets
        
        # Disable updates for performance
        self.recent_bets_table.setUpdatesEnabled(False)
        
        try:
            # Clear any existing spans
            self.recent_bets_table.clearSpans()
            
            if not bets:
                self.recent_bets_table.setRowCount(1)
                empty_item = QTableWidgetItem("No recent activity")
                empty_item.setForeground(QColor(Formatters.COLOR_GRAY))
                empty_item.setTextAlignment(Qt.AlignCenter)
                self.recent_bets_table.setSpan(0, 0, 1, len(self.TABLE_HEADERS))
                self.recent_bets_table.setItem(0, 0, empty_item)
                return
                
            # Only update the table if the number of rows has changed
            current_rows = self.recent_bets_table.rowCount()
            if current_rows != len(bets):
                self.recent_bets_table.setRowCount(len(bets))
            
            # Update each row
            for row, bet in enumerate(bets):
                self._update_table_row(row, bet)
                
        finally:
            # Re-enable updates
            self.recent_bets_table.setUpdatesEnabled(True) 

    def _handle_row_hover(self, row):
        """Handle row hover to highlight entire row"""
        if not isinstance(row, int) or row < 0 or row >= self.recent_bets_table.rowCount():
            return
            
        # Reset all rows to default background
        self._reset_all_rows()
        
        # Highlight the hovered row
        for col in range(self.recent_bets_table.columnCount()):
            item = self.recent_bets_table.item(row, col)
            if item:
                item.setBackground(QColor(self.COLOR_ROW_HOVER))

    def _handle_mouse_move(self, event):
        """Handle mouse movement to update row highlighting"""
        # Get the item under the mouse
        item = self.recent_bets_table.itemAt(event.pos())
        if item:
            # Get the row and column of the item
            row = self.recent_bets_table.row(item)
            # If we're over a valid item, highlight its row
            self._handle_row_hover(row)
        else:
            # If we're not over any item, reset all rows
            self._reset_all_rows()
        QTableWidget.mouseMoveEvent(self.recent_bets_table, event)

    def _handle_leave_event(self, event):
        """Handle mouse leaving the table"""
        self._reset_all_rows()
        QTableWidget.leaveEvent(self.recent_bets_table, event)

    def _reset_all_rows(self):
        """Reset all rows to default background"""
        for row in range(self.recent_bets_table.rowCount()):
            for col in range(self.recent_bets_table.columnCount()):
                item = self.recent_bets_table.item(row, col)
                if item:
                    item.setBackground(QColor(self.COLOR_DEFAULT_ROW)) 