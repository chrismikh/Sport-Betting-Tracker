from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QHBoxLayout,
                            QLabel, QLineEdit, QComboBox, QRadioButton,
                            QButtonGroup, QTextEdit, QPushButton, QDoubleSpinBox,
                            QFrame)
from PyQt5.QtCore import Qt, pyqtSignal, QLocale
from PyQt5.QtGui import QFont, QColor
from typing import Dict, Any, Optional
from ui.utils.formatters import Formatters
from dataclasses import dataclass
from datetime import datetime

@dataclass
class BetData:
    """Data model for bet information"""
    category: str
    sport_game: str
    tournament: str
    team_a: str
    team_b: str
    location: str
    bet: str
    bet_type: str
    odds: float
    stake: float
    result: str
    cash_out_amount: Optional[float] = None
    date: datetime = datetime.now()

class NewBetPage(QWidget):
    # Define signals
    bet_added = pyqtSignal(dict)  # Signal emitted when a new bet is added
    
    # Color constants
    COLOR_BACKGROUND = "#2a2a2a"
    COLOR_TEXT = "#ffffff"
    COLOR_INPUT = "#3a3a3a"
    COLOR_BORDER = "#4a4a4a"
    COLOR_ERROR = "#F44336"
    COLOR_SUCCESS = "#4CAF50"
    
    # Category to location mapping
    CATEGORY_LOCATIONS = {
        "Sport": "Stadium/City:",
        "Esport": "Map:"
    }
    
    # Sport and Esport options
    SPORT_OPTIONS = [
        "Football", "Basketball", "Tennis", "Baseball", "Hockey",
        "Cricket", "Rugby", "Golf", "Boxing", "MMA"
    ]
    
    ESPORT_OPTIONS = [
        "League of Legends", "Dota 2", "Counter-Strike", "Valorant",
        "Overwatch", "Rocket League", "Fortnite", "Apex Legends",
        "Starcraft", "Hearthstone"
    ]
    
    def __init__(self) -> None:
        super().__init__()
        self.bet_data = BetData(
            category="Sport",
            sport_game="",
            tournament="",
            team_a="",
            team_b="",
            location="",
            bet="",
            bet_type="Prematch",
            odds=1.0,
            stake=0.01,
            result=""
        )
        self.setup_ui()
        self.setup_connections()
        
    def setup_connections(self) -> None:
        """Setup signal connections for validation and preview"""
        self.odds_input.valueChanged.connect(self.validate_and_update_preview)
        self.stake_input.valueChanged.connect(self.validate_and_update_preview)
        self.result_combo.currentTextChanged.connect(self.validate_and_update_preview)
        self.sport_game_combo.currentTextChanged.connect(self.validate_and_update_preview)
        self.tournament_input.textChanged.connect(self.validate_and_update_preview)
        self.team_a_input.textChanged.connect(self.validate_and_update_preview)
        self.team_b_input.textChanged.connect(self.validate_and_update_preview)
        self.bet_input.textChanged.connect(self.validate_and_update_preview)
        self.location_input.textChanged.connect(self.validate_and_update_preview)
        self.category_combo.currentTextChanged.connect(self.validate_and_update_preview)
        self.live_radio.toggled.connect(self.validate_and_update_preview)
        self.prematch_radio.toggled.connect(self.validate_and_update_preview)
        self.cash_out_amount.valueChanged.connect(self.validate_and_update_preview)
        
    def setup_ui(self) -> None:
        """Setup the UI components"""
        # Main container with fixed width and height
        container = QWidget()
        container.setFixedWidth(700)
        container.setMinimumHeight(600)
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        
        # Create base fonts
        self.setup_fonts()
        
        # Create layouts
        main_layout = self.create_main_layout()
        form_preview_layout = self.create_form_preview_layout(main_layout)
        
        # Add layouts to container
        container_layout.addLayout(form_preview_layout)
        container_layout.addStretch(3)
        
        # Add buttons
        button_container = self.create_button_container()
        container_layout.addWidget(button_container)
        
        # Center the container in the window
        window_layout = QHBoxLayout()
        window_layout.setContentsMargins(80, 10, 80, 10)
        window_layout.addStretch()
        window_layout.addWidget(container)
        window_layout.addStretch()
        
        self.setLayout(window_layout)
        self.setup_styles()
        
    def setup_fonts(self) -> None:
        """Setup the fonts used in the UI"""
        self.label_font = QFont()
        self.label_font.setPointSize(14)
        
        self.input_font = QFont()
        self.input_font.setPointSize(13)
        
        self.preview_font = QFont()
        self.preview_font.setPointSize(11)
        
        self.preview_title_font = QFont()
        self.preview_title_font.setPointSize(16)
        self.preview_title_font.setBold(True)
        
        self.title_font = QFont()
        self.title_font.setPointSize(32)
        self.title_font.setBold(True)
        
        self.button_font = QFont()
        self.button_font.setPointSize(14)
        self.button_font.setBold(True)
        
    def create_main_layout(self) -> QVBoxLayout:
        """Create the main layout with title and form sections"""
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(40, 10, 40, 10)
        
        # Title
        title_label = QLabel("New Bet")
        title_label.setFont(self.title_font)
        title_label.setStyleSheet(f"color: {self.COLOR_TEXT};")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setContentsMargins(0, 0, 0, 5)
        main_layout.addWidget(title_label)
        
        # Match Information Section
        match_group = self.create_match_section()
        main_layout.addLayout(match_group)
        
        # Bet Details Section
        bet_group = self.create_bet_section()
        main_layout.addLayout(bet_group)
        
        return main_layout
        
    def create_match_section(self) -> QFormLayout:
        """Create the match information section"""
        match_group = QFormLayout()
        match_group.setSpacing(10)
        match_group.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        match_group.setContentsMargins(0, 0, 0, 8)
        
        # Category
        category_label = QLabel("Category:")
        category_label.setFont(self.label_font)
        self.category_combo = QComboBox()
        self.category_combo.addItems(self.CATEGORY_LOCATIONS.keys())
        self.category_combo.currentTextChanged.connect(self.update_location_label)
        self.category_combo.currentTextChanged.connect(self.update_sport_game_label)
        self.category_combo.setMinimumHeight(40)
        self.category_combo.setFont(self.input_font)
        match_group.addRow(category_label, self.category_combo)
        
        # Sport/Game
        self.sport_game_label = QLabel("Sport:")
        self.sport_game_label.setFont(self.label_font)
        self.sport_game_combo = QComboBox()
        self.sport_game_combo.addItems(self.SPORT_OPTIONS)
        self.sport_game_combo.setMinimumHeight(40)
        self.sport_game_combo.setFont(self.input_font)
        match_group.addRow(self.sport_game_label, self.sport_game_combo)
        
        # Tournament
        tournament_label = QLabel("Tournament:")
        tournament_label.setFont(self.label_font)
        self.tournament_input = QLineEdit()
        self.tournament_input.setMinimumHeight(40)
        self.tournament_input.setFont(self.input_font)
        match_group.addRow(tournament_label, self.tournament_input)
        
        # Match (Teams)
        match_label = QLabel("Match:")
        match_label.setFont(self.label_font)
        match_layout = QHBoxLayout()
        match_layout.setSpacing(10)
        
        self.team_a_input = QLineEdit()
        self.team_a_input.setPlaceholderText("Team A")
        self.team_a_input.setMinimumHeight(40)
        self.team_a_input.setFont(self.input_font)
        match_layout.addWidget(self.team_a_input)
        
        self.team_b_input = QLineEdit()
        self.team_b_input.setPlaceholderText("Team B")
        self.team_b_input.setMinimumHeight(40)
        self.team_b_input.setFont(self.input_font)
        match_layout.addWidget(self.team_b_input)
        
        match_group.addRow(match_label, match_layout)
        
        # Location
        self.location_input = QLineEdit()
        self.location_input.setMinimumHeight(40)
        self.location_input.setFont(self.input_font)
        self.location_label = QLabel(self.CATEGORY_LOCATIONS["Sport"])
        self.location_label.setFont(self.label_font)
        match_group.addRow(self.location_label, self.location_input)
        
        return match_group
        
    def create_bet_section(self) -> QFormLayout:
        """Create the bet details section"""
        bet_group = QFormLayout()
        bet_group.setSpacing(10)
        bet_group.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        bet_group.setContentsMargins(0, 0, 0, 8)
        
        # Bet
        bet_label = QLabel("Bet:")
        bet_label.setFont(self.label_font)
        self.bet_input = QLineEdit()
        self.bet_input.setMinimumHeight(40)
        self.bet_input.setFont(self.input_font)
        bet_group.addRow(bet_label, self.bet_input)
        
        # Type (Live/Prematch)
        type_label = QLabel("Type:")
        type_label.setFont(self.label_font)
        type_layout = QHBoxLayout()
        type_layout.setSpacing(20)
        self.type_group = QButtonGroup()
        self.prematch_radio = QRadioButton("Prematch")
        self.prematch_radio.setFont(self.input_font)
        self.live_radio = QRadioButton("Live")
        self.live_radio.setFont(self.input_font)
        self.prematch_radio.setChecked(True)
        self.type_group.addButton(self.prematch_radio)
        self.type_group.addButton(self.live_radio)
        type_layout.addWidget(self.prematch_radio)
        type_layout.addWidget(self.live_radio)
        bet_group.addRow(type_label, type_layout)
        
        # Odds
        odds_label = QLabel("Odds:")
        odds_label.setFont(self.label_font)
        self.odds_input = QDoubleSpinBox()
        self.odds_input.setRange(1.0, 1000.0)
        self.odds_input.setSingleStep(0.01)
        self.odds_input.setDecimals(2)
        self.odds_input.setMinimumHeight(40)
        self.odds_input.setFont(self.input_font)
        self.odds_input.setLocale(QLocale(QLocale.English))
        self.odds_input.setToolTip("Decimal format, e.g. 2.50")
        bet_group.addRow(odds_label, self.odds_input)
        
        # Stake
        stake_label = QLabel("Stake:")
        stake_label.setFont(self.label_font)
        self.stake_input = QDoubleSpinBox()
        self.stake_input.setRange(0.01, 1000000.0)
        self.stake_input.setSingleStep(1.0)
        self.stake_input.setDecimals(2)
        self.stake_input.setMinimumHeight(40)
        self.stake_input.setFont(self.input_font)
        self.stake_input.setLocale(QLocale(QLocale.English))
        self.stake_input.setPrefix(Formatters.CURRENCY)
        self.stake_input.setToolTip("Enter the amount you want to bet")
        bet_group.addRow(stake_label, self.stake_input)
        
        # Result
        result_label = QLabel("Result:")
        result_label.setFont(self.label_font)
        self.result_combo = QComboBox()
        self.result_combo.addItems(["", "Won", "Lost", "Cashed Out"])
        self.result_combo.currentTextChanged.connect(self.toggle_cash_out_amount)
        self.result_combo.setMinimumHeight(40)
        self.result_combo.setFont(self.input_font)
        self.result_combo.setToolTip("Select the outcome of your bet")
        bet_group.addRow(result_label, self.result_combo)
        
        # Cash Out Amount
        self.cash_out_label = QLabel("Cash Out Amount:")
        self.cash_out_label.setFont(self.label_font)
        self.cash_out_amount = QDoubleSpinBox()
        self.cash_out_amount.setRange(0.01, 1000000.0)
        self.cash_out_amount.setSingleStep(1.0)
        self.cash_out_amount.setDecimals(2)
        self.cash_out_amount.setMinimumHeight(40)
        self.cash_out_amount.setFont(self.input_font)
        
        cash_out_container = QWidget()
        cash_out_layout = QFormLayout(cash_out_container)
        cash_out_layout.setContentsMargins(0, 0, 0, 0)
        cash_out_layout.setSpacing(10)
        cash_out_layout.addRow(self.cash_out_label, self.cash_out_amount)
        self.cash_out_container = cash_out_container
        
        bet_group.addRow(cash_out_container)
        self.cash_out_container.setVisible(False)
        
        return bet_group
        
    def create_form_preview_layout(self, main_layout: QVBoxLayout) -> QHBoxLayout:
        """Create the layout containing the form and preview"""
        form_preview_layout = QHBoxLayout()
        form_preview_layout.setSpacing(40)
        
        # Form container
        form_container = QWidget()
        form_container.setFixedWidth(380)
        form_container_layout = QVBoxLayout(form_container)
        form_container_layout.setContentsMargins(0, 0, 0, 0)
        form_container_layout.addLayout(main_layout)
        
        # Preview Card
        preview_frame = self.create_preview_card()
        
        # Add form and preview to layout
        form_preview_layout.addWidget(form_container)
        form_preview_layout.addStretch(2)
        form_preview_layout.addWidget(preview_frame)
        
        return form_preview_layout
        
    def create_preview_card(self) -> QFrame:
        """Create the preview card"""
        preview_frame = QFrame()
        preview_frame.setFrameShape(QFrame.NoFrame)
        preview_frame.setMinimumWidth(300)
        preview_frame.setMaximumWidth(400)
        preview_frame.setFixedHeight(240)
        preview_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {self.COLOR_INPUT};
                border: none;
                border-radius: 0;
                padding: 3px 8px;
            }}
        """)
        preview_layout = QVBoxLayout(preview_frame)
        preview_layout.setSpacing(3)
        preview_layout.setContentsMargins(5, 1, 5, 1)
        
        self.preview_title = QLabel("Bet Preview")
        self.preview_title.setFont(self.preview_title_font)
        self.preview_title.setStyleSheet(f"color: {self.COLOR_TEXT};")
        self.preview_title.setContentsMargins(0, 0, 0, 1)
        preview_layout.addWidget(self.preview_title)
        
        self.preview_content = QLabel()
        self.preview_content.setFont(self.preview_font)
        self.preview_content.setStyleSheet(f"color: {self.COLOR_TEXT};")
        self.preview_content.setWordWrap(True)
        self.preview_content.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.preview_content.setContentsMargins(0, 1, 0, 0)
        preview_layout.addWidget(self.preview_content)
        
        return preview_frame
        
    def create_button_container(self) -> QWidget:
        """Create the button container"""
        button_container = QWidget()
        button_container.setFixedHeight(60)
        button_layout = QHBoxLayout(button_container)
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setSpacing(20)
        button_layout.setContentsMargins(40, 0, 40, 0)
        
        self.add_button = QPushButton("Add Bet")
        self.add_button.setMinimumHeight(35)
        self.add_button.setFont(self.button_font)
        self.add_button.clicked.connect(self.handle_add_bet)
        button_layout.addWidget(self.add_button)
        
        self.clear_button = QPushButton("Clear")
        self.clear_button.setMinimumHeight(35)
        self.clear_button.setFont(self.button_font)
        self.clear_button.clicked.connect(self.reset_form)
        button_layout.addWidget(self.clear_button)
        
        return button_container

    def setup_styles(self) -> None:
        """Setup the styles for all components"""
        # Base style for inputs
        input_style = f"""
            QLineEdit, QComboBox, QTextEdit, QDoubleSpinBox {{
                background-color: {self.COLOR_INPUT};
                color: {self.COLOR_TEXT};
                border: 1px solid {self.COLOR_BORDER};
                border-radius: 5px;
                padding: 5px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {self.COLOR_INPUT};
                color: {self.COLOR_TEXT};
                border: 1px solid {self.COLOR_BORDER};
                selection-background-color: {self.COLOR_BORDER};
                outline: none;
            }}
            QComboBox QAbstractItemView::item {{
                padding: 5px;
            }}
            QRadioButton {{
                color: {self.COLOR_TEXT};
                spacing: 5px;
            }}
            QPushButton {{
                background-color: {self.COLOR_INPUT};
                color: {self.COLOR_TEXT};
                border: none;
                padding: 10px;
                border-radius: 5px;
                min-width: 100px;
            }}
            QPushButton:hover {{
                background-color: {self.COLOR_BORDER};
            }}
        """
        
        self.setStyleSheet(input_style)
        
    def update_location_label(self, category: str) -> None:
        """Update the location label based on the selected category"""
        self.location_label.setText(self.CATEGORY_LOCATIONS.get(category, "Location"))
        
    def update_sport_game_label(self, category: str) -> None:
        """Update the sport/game label and options based on the selected category"""
        if category == "Sport":
            self.sport_game_label.setText("Sport:")
            self.sport_game_combo.clear()
            self.sport_game_combo.addItems(self.SPORT_OPTIONS)
        else:  # Esport
            self.sport_game_label.setText("Game:")
            self.sport_game_combo.clear()
            self.sport_game_combo.addItems(self.ESPORT_OPTIONS)
        
    def toggle_cash_out_amount(self, result: str) -> None:
        """Show/hide cash out amount field based on result selection"""
        is_cashed_out = result == "Cashed Out"
        self.cash_out_container.setVisible(is_cashed_out)
        if is_cashed_out:
            self.cash_out_amount.setValue(self.stake_input.value())  # Default to stake amount

    def handle_add_bet(self) -> None:
        """Handle the add bet button click"""
        # Validate required fields
        if not self.validate_form():
            return
            
        # Create bet data
        bet_data = {
            'category': self.category_combo.currentText(),
            'sport_game': self.sport_game_combo.currentText(),
            'tournament': self.tournament_input.text(),
            'team_a': self.team_a_input.text(),
            'team_b': self.team_b_input.text(),
            'location': self.location_input.text(),
            'bet': self.bet_input.text(),
            'type': 'Live' if self.live_radio.isChecked() else 'Prematch',
            'odds': self.odds_input.value(),
            'stake': self.stake_input.value(),
            'result': self.result_combo.currentText(),
            'cash_out_amount': self.cash_out_amount.value() if self.result_combo.currentText() == "Cashed Out" else None
        }
        
        # Emit signal with bet data
        self.bet_added.emit(bet_data)
        
        # Reset form
        self.reset_form()
        
    def handle_cancel(self) -> None:
        """Handle the cancel button click"""
        self.reset_form()
        
    def validate_form(self) -> bool:
        """Validate the form data"""
        required_fields = [
            (self.tournament_input, "Tournament"),
            (self.team_a_input, "Team A"),
            (self.team_b_input, "Team B"),
            (self.bet_input, "Bet"),
            (self.odds_input, "Odds"),
            (self.stake_input, "Stake")
        ]
        
        for field, name in required_fields:
            if isinstance(field, QLineEdit) and not field.text().strip():
                self.show_error(f"{name} is required")
                return False
            elif isinstance(field, QDoubleSpinBox) and field.value() <= 0:
                self.show_error(f"{name} must be greater than 0")
                return False
                
        return True
        
    def show_error(self, message: str) -> None:
        """Show an error message"""
        # TODO: Implement proper error dialog
        print(f"Error: {message}")
        
    def reset_form(self) -> None:
        """Reset the form to its initial state"""
        self.category_combo.setCurrentIndex(0)
        self.tournament_input.clear()
        self.team_a_input.clear()
        self.team_b_input.clear()
        self.location_input.clear()
        self.bet_input.clear()
        self.prematch_radio.setChecked(True)
        self.odds_input.setValue(1.0)
        self.stake_input.setValue(0.01)
        self.result_combo.setCurrentIndex(0)
        self.cash_out_amount.setValue(0.01)
        self.cash_out_container.setVisible(False)

    def validate_and_update_preview(self) -> None:
        """Validate inputs and update preview"""
        # Validate odds and stake
        odds_valid = self.odds_input.value() >= 1.0
        stake_valid = self.stake_input.value() > 0
        
        # Update input styles
        odds_style = f"border: 1px solid {self.COLOR_ERROR};" if not odds_valid else ""
        stake_style = f"border: 1px solid {self.COLOR_ERROR};" if not stake_valid else ""
        
        self.odds_input.setStyleSheet(odds_style)
        self.stake_input.setStyleSheet(stake_style)
        
        # Update preview
        category = self.category_combo.currentText()
        sport_game = self.sport_game_combo.currentText()
        tournament = self.tournament_input.text()
        team_a = self.team_a_input.text()
        team_b = self.team_b_input.text()
        location = self.location_input.text()
        bet = self.bet_input.text()
        bet_type = "Live" if self.live_radio.isChecked() else "Prematch"
        odds = self.odds_input.value()
        stake = self.stake_input.value()
        result = self.result_combo.currentText()
        cash_out = self.cash_out_amount.value() if result == "Cashed Out" else None
        
        preview_text = []
        if sport_game:
            # Show either Sport or Game based on category
            label = "Sport:" if category == "Sport" else "Game:"
            preview_text.append(f"{label} {sport_game}")
        if tournament:
            preview_text.append(f"Tournament: {tournament}")
        if team_a or team_b:
            match_text = f"Match: {team_a} vs {team_b}" if team_a and team_b else f"Match: {team_a or team_b}"
            preview_text.append(match_text)
        if location:
            location_label = "Stadium/City:" if category == "Sport" else "Map:"
            preview_text.append(f"{location_label} {location}")
        if bet:
            preview_text.append(f"Bet: {bet}")
        preview_text.append(f"Type: {bet_type}")
        if odds >= 1.0:
            preview_text.append(f"Odds: {odds:.2f}")
        if stake > 0:
            preview_text.append(f"Stake: {Formatters.CURRENCY}{stake:.2f}")
        if result:
            preview_text.append(f"Result: {result}")
            if result == "Cashed Out" and cash_out is not None:
                preview_text.append(f"Cash Out: {Formatters.CURRENCY}{cash_out:.2f}")
        
        self.preview_content.setText("\n".join(preview_text)) 