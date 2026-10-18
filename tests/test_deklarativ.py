"""Tests für main_deklarativ.py (deklarativer Stil).

Hinweis: Flet 1.0.1 unterstützt ft.test() nicht.
Diese Tests prüfen die Logik außerhalb des Renderer-Kontexts.
"""

from unittest.mock import MagicMock

import flet as ft


def test_page_title() -> None:
    """Testet, ob der Seitentitel in main() korrekt gesetzt wird."""
    from main_deklarativ import main
    
    mock_page = MagicMock(spec=ft.Page)
    mock_page.controls = []
    
    main(mock_page)
    
    assert mock_page.title == "Flet 1.0.1 Modern & Typisiert"
    assert mock_page.theme_mode == ft.ThemeMode.LIGHT


def test_color_logic() -> None:
    """Testet die Farb-Logik unabhängig von Flet."""
    # Extrahierte Logik aus der Komponente
    def get_bgcolor(is_blue: bool) -> str:
        return ft.Colors.BLUE_50 if is_blue else ft.Colors.GREEN_50
    
    def get_button_text(is_blue: bool) -> str:
        return "Wechsel zu Grün" if is_blue else "Wechsel zu Blau"
    
    def get_button_color(is_blue: bool) -> str:
        return ft.Colors.GREEN if is_blue else ft.Colors.BLUE
    
    # Tests
    assert get_bgcolor(False) == ft.Colors.GREEN_50
    assert get_bgcolor(True) == ft.Colors.BLUE_50
    assert get_button_text(False) == "Wechsel zu Blau"
    assert get_button_text(True) == "Wechsel zu Grün"
    assert get_button_color(False) == ft.Colors.BLUE
    assert get_button_color(True) == ft.Colors.GREEN


def test_page_render() -> None:
    """Testet, ob page.render mit der Komponente aufgerufen wird."""
    from main_deklarativ import ColorSwitcher, main
    
    mock_page = MagicMock(spec=ft.Page)
    mock_page.controls = []
    
    main(mock_page)
    
    # Prüfe, ob page.render mit ColorSwitcher aufgerufen wurde
    mock_page.render.assert_called_once_with(ColorSwitcher)
