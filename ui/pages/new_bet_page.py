from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QHBoxLayout,
                            QLabel, QLineEdit, QComboBox, QRadioButton,
                            QButtonGroup, QTextEdit, QPushButton, QDoubleSpinBox,
                            QFrame, QMessageBox, QInputDialog)
from PyQt5.QtCore import Qt, pyqtSignal, QLocale
from PyQt5.QtGui import QFont, QColor
from typing import Dict, Any, Optional, List
from ui.utils.formatters import Formatters
from dataclasses import dataclass
from datetime import datetime
from database.bet_database import BetDatabase

@dataclass
class BetDataModel:
    """Data model for bet information"""
    category: str
    sport_game: str
    team_a: str
    team_b: str
    tournament: str
    location: str
    bet_type: str
    target: str
    pick: str
    line: float
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
    
    def __init__(self) -> None:
        super().__init__()
        self.db = BetDatabase()
        self.selected_category = "Sport"
        self.selected_sport_game_id = None
        self.bet_data = BetDataModel(
            category="Sport",
            sport_game="",
            team_a="",
            team_b="",
            tournament="",
            location="",
            bet_type="",
            target="",
            pick="",
            line=0.0,
            odds=1.0,
            stake=0.01,
            result=""
        )
        self.setup_ui()
        self.setup_connections()
        self.load_categories()
        
    def setup_connections(self) -> None:
        """Setup signal connections for validation and preview"""
        self.category_combo.currentTextChanged.connect(self.load_sport_games)
        self.sport_game_combo.currentTextChanged.connect(self.on_sport_game_changed)
        self.tournament_combo.editTextChanged.connect(self.validate_and_update_preview)
        self.team_a_combo.editTextChanged.connect(self.validate_and_update_preview)
        self.team_b_combo.editTextChanged.connect(self.validate_and_update_preview)
        self.location_combo.editTextChanged.connect(self.validate_and_update_preview)
        self.bet_type_combo.currentTextChanged.connect(self.validate_and_update_preview)
        self.bet_type_combo.currentTextChanged.connect(self.update_bet_details)
        self.bet_input.textChanged.connect(self.validate_and_update_preview)
        self.bet_combo.currentTextChanged.connect(self.validate_and_update_preview)
        self.line_input.valueChanged.connect(self.validate_and_update_preview)
        self.live_radio.toggled.connect(self.validate_and_update_preview)
        self.prematch_radio.toggled.connect(self.validate_and_update_preview)
        self.odds_input.valueChanged.connect(self.validate_and_update_preview)
        self.stake_input.valueChanged.connect(self.validate_and_update_preview)
        self.result_combo.currentTextChanged.connect(self.validate_and_update_preview)
        self.result_combo.currentTextChanged.connect(self.toggle_cash_out_amount)
        self.cash_out_amount.valueChanged.connect(self.validate_and_update_preview)

    def setup_ui(self) -> None:
        """Setup the UI components"""
        # Main container with fixed width and height
        container = QWidget()
        container.setFixedWidth(1200)  # Increased total width
        container.setMinimumHeight(600)
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        
        # Create base fonts
        self.setup_fonts()
        
        # Create horizontal layout for all sections
        main_layout = QHBoxLayout()
        main_layout.setSpacing(40)  # Increased spacing between sections
        main_layout.setContentsMargins(40, 10, 40, 10)
        
        # Left Section - Match Information
        left_container = QWidget()
        left_container.setFixedWidth(350)  # Fixed width for match section
        left_layout = QVBoxLayout(left_container)
        left_layout.setSpacing(10)
        left_layout.setContentsMargins(0, 0, 0, 0)
        
        match_title = QLabel("Match Information")
        match_title.setFont(self.label_font)
        match_title.setStyleSheet(f"color: {self.COLOR_TEXT}; font-weight: bold;")
        left_layout.addWidget(match_title)
        
        match_group = self.create_match_section()
        left_layout.addLayout(match_group)
        left_layout.addStretch()
        
        main_layout.addWidget(left_container)
        
        # Middle Section - Bet Details
        middle_container = QWidget()
        middle_container.setFixedWidth(400)  # Fixed width for bet section
        middle_layout = QVBoxLayout(middle_container)
        middle_layout.setSpacing(10)
        middle_layout.setContentsMargins(0, 0, 0, 0)
        
        bet_title = QLabel("Bet Details")
        bet_title.setFont(self.label_font)
        bet_title.setStyleSheet(f"color: {self.COLOR_TEXT}; font-weight: bold;")
        middle_layout.addWidget(bet_title)
        
        bet_group = self.create_bet_section()
        middle_layout.addLayout(bet_group)
        middle_layout.addStretch()
        
        main_layout.addWidget(middle_container)
        
        # Right Section - Preview
        preview_frame = self.create_preview_card()
        main_layout.addWidget(preview_frame)
        
        # Add buttons
        button_container = self.create_button_container()
        
        # Add all sections to container
        container_layout.addLayout(main_layout)
        container_layout.addStretch(3)
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
        
    def create_match_section(self) -> QFormLayout:
        """Create the match information section (Football only)"""
        match_group = QFormLayout()
        match_group.setSpacing(15)
        match_group.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        match_group.setContentsMargins(0, 0, 0, 8)

        # Category
        category_label = QLabel("Category:")
        category_label.setFont(self.label_font)
        self.category_combo = QComboBox()
        self.category_combo.setMinimumHeight(45)
        self.category_combo.setFont(self.input_font)
        match_group.addRow(category_label, self.category_combo)

        # Sport/Game
        self.sport_game_label = QLabel("Sport/Game:")
        self.sport_game_label.setFont(self.label_font)
        self.sport_game_combo = QComboBox()
        self.sport_game_combo.setMinimumHeight(45)
        self.sport_game_combo.setFont(self.input_font)
        match_group.addRow(self.sport_game_label, self.sport_game_combo)

        # Tournament
        tournament_label = QLabel("Tournament:")
        tournament_label.setFont(self.label_font)
        self.tournament_combo = QComboBox()
        self.tournament_combo.setEditable(True)
        self.tournament_combo.setMinimumHeight(45)
        self.tournament_combo.setFont(self.input_font)
        match_group.addRow(tournament_label, self.tournament_combo)

        # Match (Teams)
        match_label = QLabel("Match:")
        match_label.setFont(self.label_font)
        match_layout = QHBoxLayout()
        match_layout.setSpacing(10)

        self.team_a_combo = QComboBox()
        self.team_a_combo.setEditable(True)
        self.team_a_combo.setPlaceholderText("Team A")
        self.team_a_combo.setMinimumHeight(45)
        self.team_a_combo.setFont(self.input_font)
        match_layout.addWidget(self.team_a_combo)

        vs_label = QLabel("vs")
        vs_label.setFont(self.label_font)
        vs_label.setAlignment(Qt.AlignCenter)
        match_layout.addWidget(vs_label)

        self.team_b_combo = QComboBox()
        self.team_b_combo.setEditable(True)
        self.team_b_combo.setPlaceholderText("Team B")
        self.team_b_combo.setMinimumHeight(45)
        self.team_b_combo.setFont(self.input_font)
        match_layout.addWidget(self.team_b_combo)

        match_group.addRow(match_label, match_layout)

        # Location
        self.location_label = QLabel("Stadium/City/Map:")
        self.location_label.setFont(self.label_font)
        self.location_combo = QComboBox()
        self.location_combo.setEditable(True)
        self.location_combo.setMinimumHeight(45)
        self.location_combo.setFont(self.input_font)
        match_group.addRow(self.location_label, self.location_combo)

        return match_group
        
    def create_bet_section(self) -> QFormLayout:
        """Create the bet details section"""
        bet_group = QFormLayout()
        bet_group.setSpacing(15)
        bet_group.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        bet_group.setContentsMargins(0, 0, 0, 8)
        
        # Bet Type
        bet_type_label = QLabel("Bet Type:")
        bet_type_label.setFont(self.label_font)
        self.bet_type_combo = QComboBox()
        self.bet_type_combo.setMinimumHeight(45)
        self.bet_type_combo.setFont(self.input_font)
        bet_group.addRow(bet_type_label, self.bet_type_combo)
        
        # Bet Section
        self.bet_label = QLabel("Bet:")
        self.bet_label.setFont(self.label_font)
        
        # Create a container for the bet input
        bet_container = QWidget()
        bet_layout = QHBoxLayout(bet_container)
        bet_layout.setContentsMargins(0, 0, 0, 0)
        bet_layout.setSpacing(0)
        
        # Create both input types but only show one at a time
        self.bet_input = QLineEdit()
        self.bet_input.setMinimumHeight(45)
        self.bet_input.setFont(self.input_font)
        
        self.bet_combo = QComboBox()
        self.bet_combo.setMinimumHeight(45)
        self.bet_combo.setFont(self.input_font)
        
        bet_layout.addWidget(self.bet_input)
        bet_layout.addWidget(self.bet_combo)
        
        bet_group.addRow(self.bet_label, bet_container)
        
        # Line Section
        self.line_label = QLabel("Line:")
        self.line_label.setFont(self.label_font)
        self.line_input = QDoubleSpinBox()
        self.line_input.setRange(-1000.0, 1000.0)
        self.line_input.setSingleStep(0.5)
        self.line_input.setDecimals(2)
        self.line_input.setMinimumHeight(45)
        self.line_input.setFont(self.input_font)
        self.line_input.setPrefix("Line: ")
        bet_group.addRow(self.line_label, self.line_input)
        
        # Bet Type (Live/Prematch)
        bet_type_container = QWidget()
        bet_type_layout = QHBoxLayout(bet_type_container)
        bet_type_layout.setContentsMargins(0, 0, 0, 0)
        bet_type_layout.setSpacing(10)
        
        self.live_radio = QRadioButton("Live")
        self.live_radio.setFont(self.input_font)
        self.prematch_radio = QRadioButton("Prematch")
        self.prematch_radio.setFont(self.input_font)
        self.prematch_radio.setChecked(True)
        
        bet_type_layout.addWidget(self.live_radio)
        bet_type_layout.addWidget(self.prematch_radio)
        bet_type_layout.addStretch()
        
        bet_group.addRow("Type:", bet_type_container)
        
        # Odds
        odds_label = QLabel("Odds:")
        odds_label.setFont(self.label_font)
        self.odds_input = QDoubleSpinBox()
        self.odds_input.setRange(1.0, 1000.0)
        self.odds_input.setSingleStep(0.1)
        self.odds_input.setDecimals(2)
        self.odds_input.setMinimumHeight(45)
        self.odds_input.setFont(self.input_font)
        bet_group.addRow(odds_label, self.odds_input)
        
        # Stake
        stake_label = QLabel("Stake:")
        stake_label.setFont(self.label_font)
        self.stake_input = QDoubleSpinBox()
        self.stake_input.setRange(0.01, 1000000.0)
        self.stake_input.setSingleStep(0.01)
        self.stake_input.setDecimals(2)
        self.stake_input.setMinimumHeight(45)
        self.stake_input.setFont(self.input_font)
        self.stake_input.setPrefix(Formatters.CURRENCY)
        bet_group.addRow(stake_label, self.stake_input)
        
        # Result
        result_label = QLabel("Result:")
        result_label.setFont(self.label_font)
        self.result_combo = QComboBox()
        self.result_combo.addItems(["Win", "Lose", "Cashed Out"])
        self.result_combo.setMinimumHeight(45)
        self.result_combo.setFont(self.input_font)
        bet_group.addRow(result_label, self.result_combo)
        
        # Cash Out Amount
        self.cash_out_container = QWidget()
        cash_out_layout = QHBoxLayout(self.cash_out_container)
        cash_out_layout.setContentsMargins(0, 0, 0, 0)
        cash_out_layout.setSpacing(0)
        
        cash_out_label = QLabel("Cash Out:")
        cash_out_label.setFont(self.label_font)
        self.cash_out_amount = QDoubleSpinBox()
        self.cash_out_amount.setRange(0.01, 1000000.0)
        self.cash_out_amount.setSingleStep(0.01)
        self.cash_out_amount.setDecimals(2)
        self.cash_out_amount.setMinimumHeight(45)
        self.cash_out_amount.setFont(self.input_font)
        self.cash_out_amount.setPrefix(Formatters.CURRENCY)
        
        cash_out_layout.addWidget(cash_out_label)
        cash_out_layout.addWidget(self.cash_out_amount)
        
        bet_group.addRow("", self.cash_out_container)
        self.cash_out_container.setVisible(False)
        
        return bet_group
        
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
        
    def load_categories(self):
        self.category_combo.clear()
        categories = set([cat for _, _, cat in self.db.get_all_sport_games()])
        for cat in sorted(categories):
            self.category_combo.addItem(cat)
        self.category_combo.setEnabled(True)
        self.category_combo.setCurrentText("Sport")
        self.load_sport_games()

    def load_sport_games(self):
        category = self.category_combo.currentText()
        self.sport_game_combo.clear()
        sport_games = self.db.get_all_sport_games(category)
        for sg_id, name, _ in sport_games:
            self.sport_game_combo.addItem(name)
        if sport_games:
            self.sport_game_combo.setCurrentIndex(0)
            self.selected_sport_game_id = sport_games[0][0]
        else:
            self.selected_sport_game_id = None
        self.load_dropdown_data()
        self.update_bet_types()

    def on_sport_game_changed(self):
        # Update selected_sport_game_id
        category = self.category_combo.currentText()
        sport_game_name = self.sport_game_combo.currentText()
        sport_games = self.db.get_all_sport_games(category)
        for sg_id, name, _ in sport_games:
            if name == sport_game_name:
                self.selected_sport_game_id = sg_id
                break
        else:
            self.selected_sport_game_id = None
        self.load_dropdown_data()
        self.update_bet_types()

    def load_dropdown_data(self) -> None:
        sport_game_id = self.selected_sport_game_id
        if not sport_game_id:
            return
        self.team_a_combo.clear()
        self.team_b_combo.clear()
        self.tournament_combo.clear()
        self.location_combo.clear()
        # Load teams
        teams = self.db.get_teams_for_sport_game(sport_game_id)
        for _, name in teams:
            self.team_a_combo.addItem(name)
            self.team_b_combo.addItem(name)
        self.team_a_combo.addItem("Add new team...")
        self.team_b_combo.addItem("Add new team...")
        self.team_a_combo.activated.connect(lambda idx: self.handle_add_new_option(self.team_a_combo, 'team'))
        self.team_b_combo.activated.connect(lambda idx: self.handle_add_new_option(self.team_b_combo, 'team'))
        # Load tournaments
        tournaments = self.db.get_tournaments_for_sport_game(sport_game_id)
        for _, name in tournaments:
            self.tournament_combo.addItem(name)
        self.tournament_combo.addItem("Add new tournament...")
        self.tournament_combo.activated.connect(lambda idx: self.handle_add_new_option(self.tournament_combo, 'tournament'))
        # Load locations
        locations = self.db.get_locations_for_sport_game(sport_game_id)
        for _, name in locations:
            self.location_combo.addItem(name)
        self.location_combo.addItem("Add new location...")
        self.location_combo.activated.connect(lambda idx: self.handle_add_new_option(self.location_combo, 'location'))

    def update_bet_types(self) -> None:
        sport_game_id = self.selected_sport_game_id
        self.bet_type_combo.clear()
        if not sport_game_id:
            return
        bet_types = self.db.get_bet_types_for_sport_game(sport_game_id)
        for _, name, description in bet_types:
            self.bet_type_combo.addItem(name)
            self.bet_type_combo.setItemData(self.bet_type_combo.count() - 1, description, Qt.ToolTipRole)

    def handle_add_new_option(self, combo: QComboBox, option_type: str):
        text_map = {
            'team': "Enter new team name:",
            'tournament': "Enter new tournament name:",
            'location': "Enter new location name:",
        }
        if combo.currentText().startswith("Add new"):
            text, ok = QInputDialog.getText(self, "Add New", text_map[option_type])
            if ok and text.strip():
                sport_game_id = self.selected_sport_game_id
                if option_type == 'team':
                    self.db.add_team(text.strip(), sport_game_id)
                    self.load_dropdown_data()
                    combo.setCurrentText(text.strip())
                elif option_type == 'tournament':
                    self.db.add_tournament(text.strip(), sport_game_id)
                    self.load_dropdown_data()
                    self.tournament_combo.setCurrentText(text.strip())
                elif option_type == 'location':
                    self.db.add_location(text.strip(), sport_game_id)
                    self.load_dropdown_data()
                    self.location_combo.setCurrentText(text.strip())

    def update_bet_details(self) -> None:
        sport_game_id = self.selected_sport_game_id
        bet_type_name = self.bet_type_combo.currentText()
        bet_type_id = self.db.get_bet_type_id(bet_type_name, sport_game_id) if sport_game_id else None
        self.bet_input.setVisible(False)
        self.bet_combo.setVisible(False)
        options = self.db.get_bet_type_options(bet_type_id) if bet_type_id else []
        if options:
            option_type = options[0][1]
            if option_type == 'dropdown':
                self.bet_combo.setVisible(True)
                self.bet_combo.clear()
                import json
                all_opts = []
                for opt in options:
                    if opt[2]:
                        try:
                            all_opts.extend(json.loads(opt[2]))
                        except Exception:
                            pass
                all_opts = list(dict.fromkeys(all_opts))
                for opt in all_opts:
                    self.bet_combo.addItem(opt)
            elif option_type == 'text':
                self.bet_input.setVisible(True)
                placeholder = options[0][3] if options[0][3] else "Enter bet option"
                self.bet_input.setPlaceholderText(placeholder)
        else:
            self.bet_input.setVisible(True)
            self.bet_input.setPlaceholderText("Enter bet option")

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

        # Determine bet_option from the visible input
        if self.bet_combo.isVisible():
            bet_option = self.bet_combo.currentText()
        else:
            bet_option = self.bet_input.text()

        # Create bet data
        bet_data = {
            'category': self.category_combo.currentText(),
            'sport_game': self.sport_game_combo.currentText(),
            'team_a': self.team_a_combo.currentText(),
            'team_b': self.team_b_combo.currentText(),
            'tournament': self.tournament_combo.currentText(),
            'location': self.location_combo.currentText(),
            'bet_type': self.bet_type_combo.currentText(),
            'bet_option': bet_option,
            'line': self.line_input.value(),
            'odds': self.odds_input.value(),
            'stake': self.stake_input.value(),
            'result': self.result_combo.currentText(),
            'cash_out_amount': self.cash_out_amount.value() if self.result_combo.currentText() == "Cashed Out" else None
        }
        
        # Save to database
        bet_id = self.db.add_bet(bet_data)
        
        if bet_id == -1:
            QMessageBox.critical(
                self,
                "Error",
                "Failed to save bet to database. Please try again."
            )
            return
            
        # Show success message
        QMessageBox.information(
            self,
            "Success",
            f"Bet has been saved successfully with ID: {bet_id}"
        )
        
        # Emit signal with bet data
        self.bet_added.emit(bet_data)
        
        # Reset form
        self.reset_form()
        # Reload dropdown data to include new entries
        self.load_dropdown_data()

    def handle_cancel(self) -> None:
        """Handle the cancel button click"""
        self.reset_form()
        
    def validate_form(self) -> bool:
        """Validate the form data"""
        required_fields = [
            (self.tournament_combo, "Tournament"),
            (self.team_a_combo, "Team A"),
            (self.team_b_combo, "Team B"),
            (self.odds_input, "Odds"),
            (self.stake_input, "Stake")
        ]

        for field, name in required_fields:
            if isinstance(field, QLineEdit) and not field.text().strip():
                self.show_error(f"{name} is required")
                return False
            elif isinstance(field, QComboBox) and not field.currentText().strip():
                self.show_error(f"{name} is required")
                return False
            elif isinstance(field, QDoubleSpinBox) and field.value() <= 0:
                self.show_error(f"{name} must be greater than 0")
                return False

        # Validate Bet field (either bet_combo or bet_input)
        if self.bet_combo.isVisible():
            if not self.bet_combo.currentText().strip():
                self.show_error("Bet option is required")
                return False
        elif self.bet_input.isVisible():
            if not self.bet_input.text().strip():
                self.show_error("Bet option is required")
                return False

        return True
        
    def show_error(self, message: str) -> None:
        """Show an error message"""
        # TODO: Implement proper error dialog
        print(f"Error: {message}")
        
    def reset_form(self) -> None:
        """Reset the form to its initial state"""
        self.category_combo.setCurrentIndex(0)
        self.tournament_combo.setCurrentText("")
        self.team_a_combo.setCurrentText("")
        self.team_b_combo.setCurrentText("")
        self.location_combo.setCurrentText("")
        self.bet_type_combo.setCurrentIndex(0)
        self.bet_input.clear()
        self.bet_combo.clear()
        self.line_input.setValue(0.0)
        self.prematch_radio.setChecked(True)
        self.odds_input.setValue(1.0)
        self.stake_input.setValue(0.01)
        self.result_combo.setCurrentIndex(0)
        self.cash_out_amount.setValue(0.01)
        self.cash_out_container.setVisible(False)

    def validate_and_update_preview(self) -> None:
        """Validate inputs and update preview"""
        # Get current values
        category = self.category_combo.currentText()
        sport_game = self.sport_game_combo.currentText()
        tournament = self.tournament_combo.currentText()
        team_a = self.team_a_combo.currentText()
        team_b = self.team_b_combo.currentText()
        location = self.location_combo.currentText()
        bet_type = self.bet_type_combo.currentText()
        line = self.line_input.value()
        odds = self.odds_input.value()
        stake = self.stake_input.value()
        result = self.result_combo.currentText()
        bet_type_radio = "Live" if self.live_radio.isChecked() else "Prematch"
        cash_out = self.cash_out_amount.value() if result == "Cashed Out" else None
        
        # Get bet value based on input type
        bet_value = ""
        if self.bet_combo.isVisible():
            bet_value = self.bet_combo.currentText()
        else:
            bet_value = self.bet_input.text()
        
        # Build preview text
        preview_text = []
        if sport_game:
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
        if bet_type:
            preview_text.append(f"Bet Type: {bet_type}")
            if bet_value or line != 0:
                bet_details = []
                if bet_value:
                    bet_details.append(bet_value)
                if line != 0:
                    bet_details.append(f"Line: {line}")
                preview_text.append(f"Bet: {' '.join(bet_details)}")
        preview_text.append(f"Type: {bet_type_radio}")
        if odds >= 1.0:
            preview_text.append(f"Odds: {odds:.2f}")
        if stake > 0:
            preview_text.append(f"Stake: {Formatters.CURRENCY}{stake:.2f}")
        if result:
            preview_text.append(f"Result: {result}")
            if result == "Cashed Out" and cash_out is not None:
                preview_text.append(f"Cash Out: {Formatters.CURRENCY}{cash_out:.2f}")
        
        # Update preview
        self.preview_content.setText("\n".join(preview_text))

    def __del__(self):
        """Cleanup when the page is destroyed"""
        if hasattr(self, 'db'):
            self.db.close() 