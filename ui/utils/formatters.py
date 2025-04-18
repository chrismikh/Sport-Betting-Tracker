from typing import Any, Dict, Optional

class Formatters:
    """Utility class for formatting values and colors"""
    
    # Constants
    CURRENCY = "$"
    POSITIVE_SYMBOL = "+"
    NEGATIVE_SYMBOL = "–"
    
    # Color constants
    COLOR_GREEN = "#4CAF50"
    COLOR_RED = "#F44336"
    COLOR_YELLOW = "#FFC107"
    COLOR_TEXT = "#ffffff"
    COLOR_BACKGROUND = "#2a2a2a"
    COLOR_BORDER = "#3a3a3a"
    COLOR_GRAY = "#888888"
    
    @classmethod
    def format_currency(cls, value: float) -> str:
        """Format a value as currency"""
        return f"{cls.CURRENCY}{abs(value):.2f}"
    
    @classmethod
    def format_profit_loss(cls, value: float) -> str:
        """Format a profit/loss value with appropriate symbol"""
        formatted = cls.format_currency(value)
        if value > 0:
            return f"{cls.POSITIVE_SYMBOL}{formatted}"
        elif value < 0:
            return f"{cls.NEGATIVE_SYMBOL}{formatted}"
        return formatted
    
    @classmethod
    def get_profit_loss_color(cls, value: float) -> str:
        """Get the color for a profit/loss value"""
        if value > 0:
            return cls.COLOR_GREEN
        elif value < 0:
            return cls.COLOR_RED
        return cls.COLOR_TEXT
    
    @classmethod
    def get_result_color(cls, result: Optional[str]) -> str:
        """Get the color for a bet result"""
        result = result.lower() if result else ''
        if result == 'won':
            return cls.COLOR_GREEN
        elif result == 'lost':
            return cls.COLOR_RED
        return cls.COLOR_YELLOW
    
    @classmethod
    def format_odds(cls, odds: Optional[float]) -> str:
        """Format odds value"""
        return f"{float(odds):.2f}" if odds is not None else '—'
    
    @classmethod
    def format_date(cls, date: Any) -> str:
        """Format date value"""
        return str(date) if date else '—' 